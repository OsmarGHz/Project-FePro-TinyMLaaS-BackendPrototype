from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import alerts, devices
from models.database import create_db_and_tables

app = FastAPI(title="TinyMLaaS Backend")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Config de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En desarrollo permitimos todo. En prod, se cambia por el dominio de React.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(alerts.router)
app.include_router(devices.router)

@app.get("/")
def root():
    return {"message": "API Backend de AgroInteligencia en línea"}