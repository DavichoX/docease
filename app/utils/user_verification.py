from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import verify_password
from app.models.users import Users
from app.schemas.users import UserInDB, UserCreate


async def verify_existing_user(user: UserCreate | UserInDB, db: AsyncSession):
    result = await db.execute(select(Users).where(Users.email == user.email))
    existing_user = result.scalars().first()
    return existing_user

async def verify_user(user_id: int, db: AsyncSession):
    result = await db.execute(select(Users).where(Users.id == user_id))
    existing_user = result.scalar_one_or_none()
    return existing_user

async def authenticate_user(username: str, password:str , db: AsyncSession):
    result = await db.execute(select(Users).where(Users.email == username))
    user = result.scalar_one_or_none()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

