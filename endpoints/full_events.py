from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from db import get_db  # Asegúrate de que tu función de conexión esté en db.py
from models.employee import EmployeeTenant
from models.events_rotations import EventRotationTenant
from sqlalchemy import insert
from datetime import date

router = APIRouter()

@router.post("/full_events/{tenant_id}")
async def create_rotation_events(tenant_id: str, db: AsyncSession = Depends(get_db)):
    # Obtener todos los empleados activos para el tenant específico
    query = select(EmployeeTenant)
    result = await db.execute(query)
    employees = result.scalars().all()

    if not employees:
        return {"message": "No active employees found for this tenant."}

    # Crear un evento de rotación para cada empleado
    events = []
    for employee in employees:
        # Creamos el evento de rotación con event_type = 1 (alta)
        event = EventRotationTenant(
            employee_id=employee.id,
            department_id=employee.department_id,
            supervisor_id=str(employee.payroll_number_boss_id),  # Si es necesario
            eventType=1,  # Esto podría ser el nombre del evento o un valor que definas
            eventDate=employee.dateHiring,  # Asumiendo que el evento se registra con la fecha de hoy
        )
        events.append(event)

    # Insertamos los eventos en la base de datos
    db.add_all(events)
    await db.commit()

    return {"message": f"Created {len(events)} rotation events."}
