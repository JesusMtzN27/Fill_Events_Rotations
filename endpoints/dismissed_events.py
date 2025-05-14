from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db import get_db
from models.employee import EmployeeTenant
from models.users import UserTenant
from models.events_rotations import EventRotationTenant

router = APIRouter()

@router.post("/dismissed_events/{tenant_id}")
async def create_dismissed_events(tenant_id: str, db: AsyncSession = Depends(get_db)):
    # Consulta empleados dados de baja: join employees con users filtrando status=False
    query = (
        select(EmployeeTenant, UserTenant)
        .join(UserTenant, EmployeeTenant.user_id == UserTenant.id)
        .where(UserTenant.status == False)
        .order_by(EmployeeTenant.id)
    )
    result = await db.execute(query)
    rows = result.all()

    if not rows:
        return {"message": f"No dismissed employees found for Tenant: {tenant_id}."}

    events = []
    for employee, user in rows:
        event = EventRotationTenant(
            employee_id=employee.id,
            department_id=employee.department_id,
            supervisor_id=str(employee.payrollNumberBoss_id),
            eventType=0,  # Indica baja
            eventDate=user.updated_at.date(),  # Solo fecha yyyy-MM-dd
            created_at=user.updated_at,  # Timestamp completo
            updated_at=user.updated_at,  # Timestamp completo
        )
        events.append(event)

    db.add_all(events)
    await db.commit()

    return {"message": f"Created {len(events)} dismissal events for Tenant: {tenant_id}."}
