# Fill_Events_Rotations
Proyecto para llenar la tabla de events_rotations de los tenants

Crear un entorno virtual:
    python -m venv venv

Activarlo:
    Windows: venv\Scripts\Activate.ps1
    Mac/Linux: source venv/bin/activate

Instalar dependencias:
    pip install -r requirements.txt

Levantar el servidor con:
    uvicorn main:app --reload