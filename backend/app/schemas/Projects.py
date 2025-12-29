from app.schemas.Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    func,
)

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cursus = Column(String, nullable=False)

    fetched_at = Column(DateTime(timezone=True), server_default=func.now())
