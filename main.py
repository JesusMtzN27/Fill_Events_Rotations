from fastapi import FastAPI
from endpoints import full_events

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Incluir los endpoints
app.include_router(full_events.router, prefix="/api", tags=["events"])

@app.get("/")
async def root():
    return {"message": "API is running!"}