from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.repositories.PostgreSQL import Base
from sqlalchemy.orm import relationship



class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    weight = Column(Integer, index=True)
    date = Column(DateTime, index=True)
    '''user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="messages")'''
