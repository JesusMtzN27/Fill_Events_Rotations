from sqlalchemy import Column, BigInteger, Boolean, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserTenant(Base):
    __tablename__ = "users"

    # Definir las columnas de la tabla
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    status = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return f"<UserTenant(id={self.id}, status={self.status})>"
