from sqlalchemy.orm import Session

from src.models.user import User
from src.schemas.user_schema import UserRegister
from src.core.security import hash_password


def create_user(db: Session, user: UserRegister):
    hashed_password = hash_password(user.password)

    new_user = User(
        username = user.username,
        email = user.email,
        password_hash = hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
