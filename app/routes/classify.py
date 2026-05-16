from fastapi import APIRouter
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/classify")
async def classify(entity_name: str, ai_system_description: str, use_case: str):
    submission_id = f"clf_{uuid.uuid4().hex[:8]}"
    return {
        "submission_id": submission_id,
        "risk_level": "limited",
        "annexes": ["I", "II"],
        "gdpr_articles": ["22", "35"],
        "dpia_required": True,
        "timestamp": datetime.utcnow().isoformat()
    }

@router.get("/classify/{submission_id}")
async def get_classification(submission_id: str):
    return {"submission_id": submission_id, "status": "complete"}
