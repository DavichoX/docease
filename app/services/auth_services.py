from app.core.security import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.utils.user_verification import authenticate_user
from datetime import timedelta
from starlette import status
from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

async def login_logic(form_data : Annotated[OAuth2PasswordRequestForm, Depends()], db : AsyncSession):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub":user.email}, expires_delta=access_token_expires)
    print(f"Token generado: {access_token}")
    return access_token
