from fastapi import FastAPI
from endpoints import full_events, dismissed_events, full_hist_rotations

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Incluir los endpoints
app.include_router(full_events.router, prefix="/api", tags=["Full Events"])
app.include_router(dismissed_events.router, prefix="/api", tags=["Full Events"])
app.include_router(full_hist_rotations.router, prefix="/api", tags=["Full Hist. Rotations"])

@app.get("/")
async def root():
    return {"message": "API is running!"}