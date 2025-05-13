# app/endpoints/events_rotations.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, sessionmaker
from database import SessionLocal, create_db_engine
from models.events_rotations import EventRotationTenant
from models.employee import EmployeeTenant
from sqlalchemy.ext.asyncio import AsyncSession
import datetime

router = APIRouter()

# Dependencia para obtener la sesión de base de datos
def get_db(tenant_id: str):
    engine = create_db_engine(tenant_id)
    session = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )()
    try:
        yield session
    finally:
        session.close()

# Crear eventos de rotación para todos los empleados de un tenant
@router.post("/full_events/{tenant_id}")
async def full_events(tenant_id: str, db: Session = Depends(get_db)):
    employees = db.query(EmployeeTenant).filter(EmployeeTenant.desactivate == False).all()  # Filtra los empleados activos
    
    events = []
    for employee in employees:
        # Suponiendo que tienes una lógica de creación de eventos para cada empleado
        event = EventRotationTenant(
            employee_id=employee.id,
            department_id=employee.department_id,
            supervisor_id=employee.payrollNumberBossId,  # Asumiendo que este es el supervisor
            eventType=1,  # Este valor debe ser definido según el tipo de evento que necesitas
            eventDate=datetime.datetime.utcnow(),
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        events.append(event)

    db.add_all(events)
    db.commit()
    return {"message": f"{len(events)} events created for all employees in tenant {tenant_id}"}
