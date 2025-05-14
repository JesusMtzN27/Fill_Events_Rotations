from sqlalchemy import Column, Date, BigInteger, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from tools.converts import DynamicSupervisorIDType

# Crear la base para las clases
Base = declarative_base()

class EmployeeTenant(Base):
    __tablename__ = "employees"

    # Definir las columnas de la tabla
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    department_id = Column(BigInteger, nullable=False)
    payrollNumberBoss_id = Column(DynamicSupervisorIDType, nullable=True)
    dateHiring = Column(Date, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return f"<EmployeeTenant(id={self.id}, user_id={self.user_id}, department_id={self.department_id})>"
