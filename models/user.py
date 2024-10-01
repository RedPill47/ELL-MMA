from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    nationality = Column(String(100))
    native_language = Column(String(50))
    purpose = Column(String(50))
    level = Column(String(20))
    created_at = Column(TIMESTAMP, server_default=func.now())

    preferences = relationship('Preference', secondary='user_preferences', back_populates='users')
    conversations = relationship('Conversation', back_populates='user')
    progress = relationship('Progress', back_populates='user')
    feedback = relationship('Feedback', back_populates='user')
