from fastapi import HTTPException
from starlette import status


def validate_email(email):
    if not "@" in email:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Email must contain '@'",
        )
    return True