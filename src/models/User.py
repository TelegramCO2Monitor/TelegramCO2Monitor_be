from sqlalchemy import BigInteger, Column, Integer, String, DateTime, Boolean
from ..repositories.PostgreSQL import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    telegram_id = Column(BigInteger, index=True)
    admin = Column(Boolean, index=True)
    active = Column(Boolean, index=True)
    phone = Column(Integer, index=True)
    registration_date = Column(DateTime, index=True)
    total_messages_weight = Column(Integer, index=True)
    email = Column(String, index=True)
