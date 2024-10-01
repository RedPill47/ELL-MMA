from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, String, Text, func
from sqlalchemy.orm import relationship
from database import Base

class Message(Base):
    __tablename__ = 'messages'

    message_id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey('conversations.conversation_id'))
    sender = Column(String(10))
    timestamp = Column(TIMESTAMP, server_default=func.now())
    content = Column(Text)
    message_type = Column(String(20))

    conversation = relationship('Conversation', back_populates='messages')