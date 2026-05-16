from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models.submission import Submission, UseCase as SubmissionUseCase
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/copilot/submit")
async def submit_copilot(
    email: str,
    company: str,
    use_case: str,
    message: str = "",
    db: Session = Depends(get_db)
):
    # Create submission in database
    submission = Submission(
        email=email,
        company=company,
        use_case=SubmissionUseCase(use_case),
        message=message if message else None
    )
    db.add(submission)
    db.commit()
    db.refresh(submission)
    
    return {
        "submission_id": str(submission.id),
        "status": "submitted",
        "onboarding_url": f"https://cognitivelogic.it/onboarding/{submission.id}",
        "estimated_time": "24-48 hours"
    }

@router.get("/copilot/submissions/{submission_id}")
async def get_submission(submission_id: str, db: Session = Depends(get_db)):
    submission = db.query(Submission).filter(Submission.id == submission_id).first()
    if not submission:
        return {"error": "Submission not found"}
    return submission.to_dict()

@router.get("/copilot/submissions")
async def list_submissions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    submissions = db.query(Submission).offset(skip).limit(limit).all()
    return {
        "total": db.query(Submission).count(),
        "items": [s.to_dict() for s in submissions]
    }
