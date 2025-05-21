from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import cast, String
from datetime import datetime
from db import get_db
from models.events_rotations import EventRotationTenant
from models.users import UserTenant

router = APIRouter()

@router.post("/update_supervisor_names/{tenant_id}")
async def update_supervisor_names(tenant_id: str, db: AsyncSession = Depends(get_db)):
    try:
        events_q = await db.execute(select(EventRotationTenant))
        events = events_q.scalars().all()
        if not events:
            return {"message": f"No events_rotations records found for tenant {tenant_id}."}

        supervisor_cache = {}
        updated_count = 0

        for event in events:
            sup_id = event.supervisor_id
            if sup_id is None:
                continue

            if sup_id in supervisor_cache:
                full_name = supervisor_cache[sup_id]
            else:
                user_q = await db.execute(
                    select(UserTenant.fullName)
                    .where(cast(UserTenant.payrollNumber, String) == sup_id)
                )
                user = user_q.scalar_one_or_none()
                full_name = user if user else None
                supervisor_cache[sup_id] = full_name

            if full_name and event.supervisorName != full_name:
                event.supervisorName = full_name
                event.updated_at = datetime.utcnow()
                updated_count += 1

        if updated_count > 0:
            await db.commit()

        return {
            "message": f"Supervisor names updated for tenant {tenant_id}.",
            "updated_records": updated_count,
            "total_records": len(events)
        }
    except Exception as e:
        # Para depurar, devuelve el error
        raise HTTPException(status_code=500, detail=str(e))
