from fastapi import HTTPException
from starlette import status

def validate_email(email):
    if not "@" in email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= "Email must contain '@'",
        )