from sqlalchemy import Column, Integer, String, DateTime, Boolean
from src.repositories.PostgreSQL import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    telegram_id = Column(Integer, unique=True, index=True)
    name = Column(String, index=True)
    admin = Column(Boolean, default=False, index=True)
    active = Column(Boolean, default=True, index=True)
    phone = Column(Integer, index=True, nullable=True)
    registration_date = Column(DateTime, index=True)
    total_messages_weight = Column(Integer, default=0, index=True)
    email = Column(String, index=True, nullable=True)
