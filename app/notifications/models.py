from sqlalchemy import Column, DateTime, Integer, String, func
from app.database import Base



class Notification(Base):
    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True, nullable=False)
    status = Column(String, nullable=False)
    task_type = Column(String, nullable=False)
    to = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(String, nullable=False)
    error_message = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
