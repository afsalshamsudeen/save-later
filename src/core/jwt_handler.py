from datetime import datetime, timedelta, UTC
from jose import jwt

from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGIRTHM = os.getenv("ALGORITHM")
EXPIRE_TIME = int(os.getenv("TOKEN_EXPIRES_IN_MINUTES",60)
)
def create_access_token(data: dict):
    to_encode = data.copy()

    expire_time =datetime.now(UTC) + timedelta(
        minutes=EXPIRE_TIME
    )
    to_encode.update({
        "exp":expire_time
    }) 

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGIRTHM
    )

    return encoded_jwt

#print(SECRET_KEY)