from fastapi import APIRouter, Depends
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

workspaces = APIRouter()

async def save_workspace_settings():
    pass

async def get_workspace_settings():
    pass