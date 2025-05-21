from sqlalchemy import Column, BigInteger, Boolean, TIMESTAMP, String
from sqlalchemy.orm import declarative_base
from tools.converts import DynamicSupervisorIDType


Base = declarative_base()

class UserTenant(Base):
    __tablename__ = "users"

    # Definir las columnas de la tabla
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    payrollNumber = Column(DynamicSupervisorIDType, nullable=True)
    fullName = Column(String(255), nullable=True)  # Solo como referencia del jefe
    status = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return f"<UserTenant(id={self.id}, status={self.status})>"
