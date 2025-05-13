# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Crear una base para los modelos
Base = declarative_base()

# Establecer el URL dinámico para la base de datos según el tenant_id
def get_database_url(tenant_id: str):
    return f"postgresql://postgres:uE240F9l@operaria-db-green-gqrvex.clk2smu4o206.us-east-1.rds.amazonaws.com:5432/{tenant_id}"

# Crear un motor dinámico de conexión a la base de datos
def create_db_engine(tenant_id: str):
    database_url = get_database_url(tenant_id)
    return create_engine(database_url, connect_args={"check_same_thread": False})

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=create_db_engine)
