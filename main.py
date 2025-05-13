# app/main.py
from fastapi import FastAPI
from endpoints import employees, events_rotations

app = FastAPI()

# Incluir los endpoints
app.include_router(employees.router)
app.include_router(events_rotations.router)
