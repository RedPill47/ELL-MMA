from sqlalchemy import Column, Integer, ForeignKey, String, DECIMAL, Interval, TIMESTAMP, func
from sqlalchemy.orm import relationship
from database import Base

class Progress(Base):
    __tablename__ = 'progress'

    progress_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    lesson_id = Column(Integer, ForeignKey('lessons.lesson_id'))
    activity_id = Column(Integer, ForeignKey('activities.activity_id'))
    status = Column(String(20))
    score = Column(DECIMAL(5, 2))
    time_spent = Column(Interval)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user = relationship('User', back_populates='progress')
    lesson = relationship('Lesson', back_populates='progress')
    activity = relationship('Activity', back_populates='progress')