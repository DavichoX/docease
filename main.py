from fastapi import FastAPI,Depends
from app.routes.users import users
from app.routes.auth import auth, oauth2_scheme
#from app.core.security import verify_token
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

allowed_origins:list[str] = [
    "http://localhost:5173/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"hello": "world"}

app.include_router(users, prefix="/users")
app.include_router(auth, prefix="/auth")