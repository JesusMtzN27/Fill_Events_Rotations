from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from sqlalchemy import MetaData

# Función para obtener la URL de conexión a la base de datos para cada tenant
def get_database_url(tenant_id: str) -> str:
    # Aquí puedes personalizar la URL dependiendo del tenant_id
    return f"postgresql+asyncpg://postgres:uE240F9l@operaria-db-green-gqrvex.clk2smu4o206.us-east-1.rds.amazonaws.com:5432/{tenant_id}"

# Crear el motor de conexión a la base de datos
def create_db_engine(tenant_id: str):
    database_url = get_database_url(tenant_id)
    engine = create_async_engine(database_url, echo=True, future=True)
    return engine

# Crear una sesión de base de datos asíncrona
def create_db_session(tenant_id: str):
    engine = create_db_engine(tenant_id)
    Session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    return Session

# Función para cerrar la sesión (usando async)
async def close_db_session(session: AsyncSession):
    await session.close()

# Función para obtener la sesión de base de datos
# Usamos un generador para garantizar el ciclo de vida de la sesión
async def get_db(tenant_id: str):
    Session = create_db_session(tenant_id)
    async with Session() as session:
        yield session
