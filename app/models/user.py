from uuid import uuid4

from sqlalchemy import Boolean, Column, String

from app.models.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True, default=uuid4())
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    team = Column(String)
    is_user_active = Column(Boolean, default=True)
    hashed_password = Column(String)
