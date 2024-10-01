from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base

class Agent(Base):
    __tablename__ = 'agents'

    agent_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)

    feedback = relationship('Feedback', back_populates='agent')