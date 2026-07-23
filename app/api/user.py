from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate
from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
)

router = APIRouter(
    tags=["👤 Users"],
)


@router.post("/users")
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)


@router.get("/users")
def read_users(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get("/users/{user_id}")
def read_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_by_id(db, user_id)
