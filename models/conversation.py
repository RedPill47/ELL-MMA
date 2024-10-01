from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, String, func
from sqlalchemy.orm import relationship
from database import Base

class Conversation(Base):
    __tablename__ = 'conversations'

    conversation_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    start_time = Column(TIMESTAMP, server_default=func.now())
    end_time = Column(TIMESTAMP)
    status = Column(String(20))

    user = relationship('User', back_populates='conversations')
    messages = relationship('Message', back_populates='conversation')