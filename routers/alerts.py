from fastapi import APIRouter

router = APIRouter(prefix="/api/alerts", tags=["Alerts"])

@router.get("/")
def get_mock_alerts():
    # Mock data de alertas para el dashboard
    return [
        {"id": 1, "severity": "critical", "message": "Pest detected in Sector 4", "timestamp": "2026-07-30T10:00:00Z"},
        {"id": 2, "severity": "warning", "message": "Low moisture level detected", "timestamp": "2026-07-30T11:20:00Z"}
    ]