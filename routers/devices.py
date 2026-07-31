from fastapi import APIRouter

router = APIRouter(prefix="/api/devices", tags=["Devices"])

@router.get("/")
def get_mock_devices():
    # Mock data de nodos / dispositivos IoT
    return [
        {"id": 1, "name": "Nodo de campo Autónomo 1", "status": "online", "battery": "85%"},
        {"id": 2, "name": "Nodo de campo Autónomo 2", "status": "offline", "battery": "12%"}
    ]