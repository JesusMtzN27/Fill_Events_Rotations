from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from tools.converts import DynamicSupervisorIDType

# Crear la base para las clases
Base = declarative_base()

class EmployeeTenant(Base):
    __tablename__ = "employees"

    # Definir las columnas de la tabla
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    department_id = Column(Integer, nullable=False)
    payroll_number_boss_id = Column(DynamicSupervisorIDType, nullable=True)
    dateHiring = Column(Date, nullable=True)

    def __repr__(self):
        return f"<EmployeeTenant(id={self.id}, user_id={self.user_id}, department_id={self.department_id})>"
