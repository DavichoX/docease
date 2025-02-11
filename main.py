from fastapi import FastAPI,Depends
from app.routes.users import users
from app.routes.auth import auth, oauth2_scheme
#from app.core.security import verify_token

app = FastAPI()

@app.get("/")
async def read_root():
    return {"hello": "world"}

app.include_router(users, prefix="/users")
app.include_router(auth, prefix="/auth")