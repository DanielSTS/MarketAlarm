from sqlalchemy import Column, String, Float, ForeignKey, LargeBinary, UUID
from sqlalchemy.orm import relationship, declarative_base
import uuid

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(LargeBinary, nullable=False)
    password_salt = Column(LargeBinary, nullable=False)

    alarms = relationship("AlarmModel", back_populates="user")


class AlarmModel(Base):
    __tablename__ = 'alarms'

    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(), ForeignKey('users.id'), nullable=False)
    asset = Column(String(255), nullable=False)
    target_price = Column(Float, nullable=False)

    user = relationship("UserModel", back_populates="alarms")
