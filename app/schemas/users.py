from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "admin",
                "email": "<EMAIL>",
            }
        }

class UserCreate(UserBase):
    username: str
    email: str
    password: str
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "<NAME>",
                "email": "<EMAIL>",
                "password": "<PASSWORD>",
            }
        }

class UserInDB(UserBase):
    id: int
    hashed_password: str
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "hashed_password": "<PASSWORD>",
            }
        }