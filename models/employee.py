# app/models/employees.py
from sqlalchemy import Column, Integer, String, SmallInteger, Boolean, DateTime, Date
from database import Base
from datetime import datetime
from tools.converts import DynamicNumberType  # Asegúrate de que esta ruta sea correcta

class EmployeeTenant(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    department_id = Column(Integer, nullable=True)
    typeUnion = Column(SmallInteger, nullable=True)
    scholarship = Column(SmallInteger, nullable=True)
    gender = Column(SmallInteger, nullable=True)
    typeEmployee = Column(SmallInteger, nullable=True)
    workModality = Column(SmallInteger, nullable=True)
    maritalStatus = Column(SmallInteger, nullable=True)
    desactivate = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    payrollNumberBossId = Column(DynamicNumberType, nullable=True)  # Asumido como tipo personalizado
    dateHiring = Column(Date, nullable=True)  # Fecha de contratación
