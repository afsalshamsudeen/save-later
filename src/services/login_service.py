from sqlalchemy.orm import Session
from src.schemas.user_schema import UserLogin
from src.models.user import User
from src.core.security import verify_password
from fastapi import HTTPException

def login_user(db: Session, user_data: UserLogin):

    user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="email is incorrect"
        )
    

    if not verify_password(user_data.password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"

        )
    
    return user
