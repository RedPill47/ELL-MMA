from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Activity(Base):
    __tablename__ = 'activities'

    activity_id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey('lessons.lesson_id'))
    title = Column(String(200))
    activity_type = Column(String(50))
    description = Column(Text)
    vector_db_reference = Column(String(255))

    lesson = relationship('Lesson', back_populates='activities')
    progress = relationship('Progress', back_populates='activity')