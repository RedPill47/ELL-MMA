from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Preference(Base):
    __tablename__ = 'preferences'

    preference_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)

    users = relationship('User', secondary='user_preferences', back_populates='preferences')
