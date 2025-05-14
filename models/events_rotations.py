from sqlalchemy import Column, Integer, String, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base

# Crear la base para las clases
Base = declarative_base()

class EventRotationTenant(Base):
    __tablename__ = "events_rotations"

    # Definir las columnas de la tabla
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    employee_id = Column(BigInteger, nullable=False)  # Solo como referencia del empleado
    department_id = Column(BigInteger, nullable=False)  # Solo como referencia del departamento
    # supervisor_id = Column(String, nullable=True)  # Solo como referencia del jefe
    eventType = Column(BigInteger, nullable=False)
    eventDate = Column(Date, nullable=False)

    def __repr__(self):
        return f"<EventRotationTenant(id={self.id}, employee_id={self.employee_id}, event_type={self.event_type})>"
