from datetime import datetime, timedelta, UTC
from jose import jwt

from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGIRTHM = os.getenv("ALGORITHM")
EXPIRE_TIME = os.getenv("TOKEN_EXPIRES_IN_MINUTES")

print(SECRET_KEY)