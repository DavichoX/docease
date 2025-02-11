from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings
from datetime import timezone, timedelta, datetime

SECRET_KEY = settings.SECRET_KEY

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

context_schema = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str):
    return context_schema.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return context_schema.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy() # copia los datos ingresados por parametro
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt





