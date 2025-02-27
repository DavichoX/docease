from fastapi import APIRouter, Depends
from sqlalchemy.sql.functions import current_user

from app.schemas.documents import DocumentCreate, Document
from app.services.auth_services import get_current_user
from app.services.users_service import register_user, delete_user
from app.schemas.users import UserCreate, UserInDB
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.documents_services import create_document, get_document

documents = APIRouter()

@documents.post("/", response_model=Document)
async def create_document_endpoint(document: DocumentCreate,
                                   db: AsyncSession = Depends(get_db),
                                   current: UserInDB = Depends(get_current_user())):

    document.created_by = current.id
    document.updated_by = current.id

    return create_document(document=document, db=db)