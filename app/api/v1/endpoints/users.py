import logging
from hashlib import md5
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.schemas.user_request import UserRequest
from app.api.v1.schemas.user_response import UserResponse
from app.models.base import SessionLocal
from app.models.user import User

logger = logging.getLogger(name="__main__")
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users", status_code=204)
@router.post("/users/", status_code=204)
async def create_user(request: UserRequest, db: Session = Depends(get_db)):
    hashed_pw = md5(request.password.encode("utf-8")).hexdigest()
    new_user = User(
        id=request.id,
        email=request.email,
        first_name=request.first_name,
        last_name=request.last_name,
        team=request.team,
        hashed_password=hashed_pw,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


@router.get("/users", status_code=200, response_model=List[UserResponse])
@router.get("/users/", status_code=200, response_model=List[UserResponse])
async def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 20):
    return db.query(User).offset(skip).limit(limit).all()


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(email: str, db: Session = Depends(get_db)):
    db.delete(db.query(User).filter(User.email == email).first())
    db.commit()
