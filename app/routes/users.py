from fastapi import APIRouter, Depends
from app.services.users_service import register_user, delete_user
from app.schemas.users import UserCreate
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

users = APIRouter()

@users.post("/register/")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    await register_user(user,db)
    return {"message": "User registered"}

@users.delete("/{user_id}/")
async def delete(user_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await delete_user(user_id,db)
    if not deleted:
        return {"message": "User not found"}
    return {"message": "User deleted"}


