from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship
from database import Base

class Lesson(Base):
    __tablename__ = 'lessons'

    lesson_id = Column(Integer, primary_key=True, index=True)
    kapitel = Column(String(100))
    thema = Column(String(100))
    title = Column(String(200))
    description = Column(Text)
    vector_db_reference = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())

    activities = relationship('Activity', back_populates='lesson')
    progress = relationship('Progress', back_populates='lesson')