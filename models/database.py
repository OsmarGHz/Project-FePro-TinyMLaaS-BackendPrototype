from sqlmodel import SQLModel, create_engine
from models.schema import Device, Telemetry, Alert  # noqa: F401 – necesario para que SQLModel registre las tablas
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()

raw_password = os.getenv("DB_PASSWORD")

if not raw_password:
    raise ValueError("No se encontró DB_PASSWORD en el archivo .env")

_password = urllib.parse.quote_plus(raw_password)

DATABASE_URL = f"postgresql://postgres:{_password}@localhost:5432/tinymlaas_db"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)