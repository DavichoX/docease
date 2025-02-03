from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer


oauth2_schema = OAuth2PasswordBearer(tokenUrl="/login")

auth = APIRouter()


@auth.get("/login")
async def login():
    pass

