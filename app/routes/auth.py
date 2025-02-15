from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import  OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.Token import Token
from app.services.auth_services import login_logic
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

auth = APIRouter()

@auth.post("/login")
async def login(form_data : Annotated[OAuth2PasswordRequestForm, Depends()], db : AsyncSession = Depends(get_db)) -> Token:
    access_token = await login_logic(form_data, db)
    return Token(access_token=access_token, token_type="Bearer")

