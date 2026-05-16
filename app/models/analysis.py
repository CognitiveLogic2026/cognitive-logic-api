from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Enum as SQLEnum, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.models.database import Base
import enum

class RiskLevel(str, enum.Enum):
    PROHIBITED = "prohibited"
    HIGH = "high"
    LIMITED = "limited"
    MINIMAL = "minimal"

class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    submission_id = Column(UUID(as_uuid=True), ForeignKey("submissions.id"))
    entity_name = Column(String)
    entity_type = Column(String)
    qen_score = Column(Float, default=0.0)
    risk_classification = Column(SQLEnum(RiskLevel), default=RiskLevel.MINIMAL)
    brain_a_result = Column(JSON, nullable=True)
    brain_b_result = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.id),
            "submission_id": str(self.submission_id),
            "entity_name": self.entity_name,
            "entity_type": self.entity_type,
            "qen_score": self.qen_score,
            "risk_classification": self.risk_classification.value,
            "brain_a_result": self.brain_a_result,
            "brain_b_result": self.brain_b_result,
            "created_at": self.created_at.isoformat()
        }
