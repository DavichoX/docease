from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from app.schemas.users import UserCreate
from app.models.users import Users
from app.core.security import get_hashed_password
from app.utils.user_verification import verify_existing_user, verify_user
from app.utils.email_validator import validate_email

async def register_user(user: UserCreate, db: AsyncSession):
    await validate_email(user.email)
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


