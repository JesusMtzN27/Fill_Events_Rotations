# Fill_Events_Rotations
Proyecto para llenar la tabla de events_rotations de los tenants

Crear un entorno virtual:
    python -m venv venv

Activarlo:
    Windows: venv\Scripts\Activate.ps1
    Mac/Linux: source venv/bin/activate

Instalar dependencias:
    pip install -r requirements.txt

    pip install fastapi[all] sqlalchemy
    pip install python-dotenv
    pip install asyncpg


Levantar el servidor con:
    uvicorn main:app --reload
