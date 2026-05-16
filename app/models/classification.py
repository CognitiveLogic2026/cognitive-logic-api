from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Enum as SQLEnum, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.models.database import Base
import enum

class RiskClassification(str, enum.Enum):
    PROHIBITED = "prohibited"
    HIGH = "high"
    LIMITED = "limited"
    MINIMAL = "minimal"

class Classification(Base):
    __tablename__ = "classifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    submission_id = Column(UUID(as_uuid=True), ForeignKey("submissions.id"))
    ai_system_name = Column(String)
    risk_level = Column(SQLEnum(RiskClassification), default=RiskClassification.MINIMAL)
    annexes = Column(JSON, default=list)
    gdpr_articles = Column(JSON, default=list)
    dpia_required = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.id),
            "submission_id": str(self.submission_id),
            "ai_system_name": self.ai_system_name,
            "risk_level": self.risk_level.value,
            "annexes": self.annexes,
            "gdpr_articles": self.gdpr_articles,
            "dpia_required": self.dpia_required,
            "created_at": self.created_at.isoformat()
        }
