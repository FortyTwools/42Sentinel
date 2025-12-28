from app.schemas.Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    Float,
    Boolean,
    DateTime,
    JSON,
    func,
    ForeignKey,
)

class ProcessedUser(Base):
    __tablename__ = "processed_users"

    id = Column(Integer, ForeignKey("ft_users.id"), primary_key=True)
    ft_user = relationship("FtUser", back_populates="processed", uselist=False)

    raw_logtime = Column(JSON, nullable=False) #keep dict of logtime
    raw_evals = Column(JSON, nullable=False) #keep dict of evals

    #evalutor card
    evaluator_total_evals = Column(Integer, nullable=True)
    evaluator_avg_time = Column(Integer, nullable=True)
    evaluator_avg_grade = Column(Float, nullable=True)
    evaluator_invalid_evals = Column(Integer, nullable=True)
    evaluator_top = Column(JSON, nullable=True)
    # column containing: pp_micro, intra, number of evaluations by evalutor on them, average grade of all those evals

    #evalutee card
    evaluatee_total_evals = Column(Integer, nullable=True)
    evaluatee_avg_time = Column(Integer, nullable=True)
    evaluatee_avg_grade = Column(Float, nullable=True)
    evaluatee_epp = Column(Integer, nullable=True)
    evaluatee_top = Column(JSON, nullable=True)
    # column containing: pp_micro, intra, number of evaluations by evalutee on them, average grade of all those evals

    #dashboard:
    #flags
    outercore = Column(Boolean, default=False)
    night_stud = Column(Boolean, default=False)
    rank = Column(Integer, nullable=False)
    evals_not_at_school = Column(Integer, default=False)

    processed_logtime = Column(JSON, nullable=True)
    processed_evals = Column(JSON, nullable=True)

    fetched_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

