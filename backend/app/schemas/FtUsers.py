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

class FtUser(Base):
    __tablename__ = "ft_users"

    id = Column(Integer, primary_key=True)
    processed = relationship("ProcessedUser", back_populates="ft_user", uselist=False)

    name = Column(String, nullable=False)
    login = Column(String, nullable=False)

    image_link = Column(String, nullable=True)
    image_large = Column(String, nullable=True)
    image_medium = Column(String, nullable=True)
    image_small = Column(String, nullable=True)
    image_micro = Column(String, nullable=True)

    staff = Column(Boolean, nullable=False)
    active = Column(Boolean, nullable=False)
    fetched_at = Column(DateTime, server_default=func.now())
