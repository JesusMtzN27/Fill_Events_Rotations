# app/models/events_rotations.py
from sqlalchemy import Column, Integer, BigInteger, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class EventRotationTenant(Base):
    __tablename__ = "events_rotations"

    id = Column(Integer, primary_key=True, autoincrement=True)  # ID único
    employee_id = Column(BigInteger, ForeignKey('employees.id'), nullable=False)  # Relación con Employee
    department_id = Column(BigInteger, ForeignKey('employees.department_id'), nullable=False)  # Relación con Department
    supervisor_id = Column(BigInteger, ForeignKey('employees.payrollNumberBossId'), nullable=True)  # Relación con Supervisor (nullable)
    eventType = Column(Integer, nullable=True)  # Tipo de evento
    eventDate = Column(Date, nullable=False)  # Fecha del evento
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)  # Fecha de creación
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)  # Fecha de actualización

    # Relación con la tabla employees
    employee = relationship("EmployeeTenant", back_populates="events")
