from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    id: Optional[str] = uuid4()
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    team: str


__all__ = ["UserRequest"]
