from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    team: str
    is_user_active: bool = True
    hashed_password: str

    class Config:
        orm_mode = True


__all__ = ["UserResponse"]
