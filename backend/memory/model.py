import uuid
from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Memory(Base):
    __tablename__ = "memories"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(100), nullable=False, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)