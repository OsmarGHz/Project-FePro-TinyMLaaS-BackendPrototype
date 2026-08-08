from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# Tabla para los dispositivos IoT (Nodos de campo)
class Device(SQLModel, table=True):
    __tablename__ = "devices"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    status: str = Field(default="offline")
    battery_level: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Tabla para la Telemetría (Lecturas de humedad, temperatura, etc.)
class Telemetry(SQLModel, table=True):
    __tablename__ = "telemetry"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: int = Field(foreign_key="devices.id") # Relación con la tabla devices
    soil_moisture: float
    temperature: Optional[float] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

# Tabla para las Alertas del Sistema
class Alert(SQLModel, table=True):
    __tablename__ = "alerts"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: int = Field(foreign_key="devices.id") # Relación con la tabla devices
    severity: str # Ej: "critical", "warning", "info"
    message: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)