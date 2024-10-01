from sqlalchemy import Column, Integer, ForeignKey, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship
from database import Base

class Feedback(Base):
    __tablename__ = 'feedback'

    feedback_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    agent_id = Column(Integer, ForeignKey('agents.agent_id'))
    content = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship('User', back_populates='feedback')
    agent = relationship('Agent', back_populates='feedback')