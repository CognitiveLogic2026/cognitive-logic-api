from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "Cognitive Logic API v1.0",
        "timestamp": datetime.utcnow().isoformat()
    }

@router.get("/status")
async def status():
    return {
        "status": "operational",
        "brains": {"brain_a": "Claude", "brain_b": "Gemini"}
    }
