from fastapi import HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from app.core.database import get_db
from app.schemas.users import UserCreate
from app.models.users import Users
from app.core.security import get_hashed_password, SECRET_KEY, ALGORITHM
from app.utils.user_verification import verify_existing_user, verify_user
from app.utils.email_validator import validate_email
from jose import jwt, JWTError
from app.routes.auth import oauth2_scheme

async def register_user(user: UserCreate, db: AsyncSession):
    validate_email(user.email)
    existing_user = await verify_existing_user(user,db)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )
    new_user = Users(
        username=user.username,
        email=user.email,
        hashed_password = get_hashed_password(user.password),
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def delete_user(user: int, db: AsyncSession):
    existing_user = verify_user(user, db)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    await db.delete(existing_user)
    await db.commit()
    return True


async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exceptions
    except JWTError:
        raise credentials_exceptions
    user = verify_existing_user(username, db)
    if user is None:
        raise credentials_exceptions
    return user


