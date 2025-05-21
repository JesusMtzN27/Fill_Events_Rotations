from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func, extract
from datetime import date, datetime
from db import get_db
from models.events_rotations import EventRotationTenant
from models.history_rotations import HistoryRotationTenant

router = APIRouter()

@router.post("/full_hist_rotations/{tenant_id}")
async def calculate_rotation_summary(tenant_id: str, db: AsyncSession = Depends(get_db)):

    # Obtener primer fecha de evento para tenant
    first_date_q = await db.execute(
        select(func.min(EventRotationTenant.eventDate))
    )
    first_date = first_date_q.scalar()
    if first_date is None:
        raise HTTPException(status_code=404, detail="No event records found for tenant")

    # Fecha actual
    today = date.today()

    # Crear rango mensual desde primer mes hasta mes actual
    # Ejemplo: [(2023,1), (2023,2), ..., (2025,5)]
    months_range = []
    year = first_date.year
    month = first_date.month
    while (year, month) <= (today.year, today.month):
        months_range.append((year, month))
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    # Consultar resumen por mes y tipo evento para tenant
    # Agrupar por año, mes, eventType y contar registros
    events_q = await db.execute(
        select(
            extract('year', EventRotationTenant.eventDate).label('year'),
            extract('month', EventRotationTenant.eventDate).label('month'),
            EventRotationTenant.eventType,
            func.count().label('count')
        )
        # Agregar filtro tenant_id si aplica
        .group_by('year', 'month', EventRotationTenant.eventType)
        .order_by('year', 'month')
    )
    events_data = events_q.all()

    # Organizar datos en diccionario: {(year, month): {entries: n, exits: n}}
    summary = {}
    for year_f, month_f, event_type, count in events_data:
        key = (int(year_f), int(month_f))
        if key not in summary:
            summary[key] = {"entries": 0, "exits": 0}
        if event_type == 1:
            summary[key]["entries"] += count
        elif event_type == 0:
            summary[key]["exits"] += count

    # Calcular initial y total por mes, incluyendo meses sin datos (usar months_range)
    results = []
    prev_total = 0
    for (y, m) in months_range:
        entries = summary.get((y, m), {}).get("entries", 0)
        exits = summary.get((y, m), {}).get("exits", 0)
        initial = prev_total
        total = initial + entries - exits

        results.append({
            "year": y,
            "month": m,
            "initial": initial,
            "entries": entries,
            "exits": exits,
            "total": total,
        })

        prev_total = total

    # Guardar o actualizar en history_rotations
    for record in results:
        # Buscar si ya existe registro para mes y año
        existing = await db.execute(
            select(HistoryRotationTenant)
            .where(HistoryRotationTenant.year == record["year"])
            .where(HistoryRotationTenant.month == record["month"])
        )
        existing_record = existing.scalar_one_or_none()

        if existing_record:
            # Actualizar
            existing_record.initial = record["initial"]
            existing_record.entries = record["entries"]
            existing_record.exits = record["exits"]
            existing_record.total = record["total"]
            existing_record.updated_at = datetime.utcnow()
        else:
            # Insertar nuevo
            new_record = HistoryRotationTenant(
                year=record["year"],
                month=record["month"],
                initial=record["initial"],
                entries=record["entries"],
                exits=record["exits"],
                total=record["total"],
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
                deleted_at=None,
            )
            db.add(new_record)

    await db.commit()

    return {"message": f"Rotation summary calculated and saved for tenant {tenant_id}."}
    # return {"message": f"Rotation summary calculated and saved for tenant {tenant_id}.", "data": results}
