from sqlalchemy import Column, Integer, String, Date, BigInteger, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

# Crear la base para las clases
Base = declarative_base()

class HistoryRotationTenant(Base):
    __tablename__ = "history_rotations"

    # Definir las columnas de la tabla
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    initial = Column(Integer, nullable=False)
    entries = Column(Integer, nullable=False)
    exits = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    deleted_at = Column(TIMESTAMP, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return f"<HistoryRotationTenant(id={self.id}, initial={self.initial}, entries={self.entries}, exits={self.exits}, total={self.total}, month={self.month}, year={self.year})>"
