from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.schemas.user_schema import (
    UserRegister,
    UserResponse,
    UserLogin
)

from src.services.auth_services import create_user
from src.services.login_service import login_user
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/signup",
    response_model=UserResponse
)
def register(user:UserRegister ,db:Session = Depends(get_db)):
    return create_user(db, user)

@router.post("/login")
def login(
    user_data:UserLogin,
    db:Session = Depends(get_db)
          ):
    return login_user(db, user_data)