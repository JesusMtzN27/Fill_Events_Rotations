# app/models/employee.py
from sqlalchemy import Column, BigInteger, SmallInteger, Boolean, TIMESTAMP, Date
from sqlalchemy.orm import declarative_base
from datetime import datetime
from tools.converts import DynamicNumberType
from database import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, nullable=False)
    department_id = Column(BigInteger, nullable=True)
    typeUnion = Column(SmallInteger, nullable=True)
    scholarship = Column(SmallInteger, nullable=True)
    gender = Column(SmallInteger, nullable=True)
    typeEmployee = Column(SmallInteger, nullable=True)
    workModality = Column(SmallInteger, nullable=True)
    maritalStatus = Column(SmallInteger, nullable=True)
    desactivate = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    payrollNumberBoss_id = Column(DynamicNumberType, nullable=True)  # id del Jefe Imnediato
    dateHiring = Column(Date, nullable=True)  # Fecha de contratación
