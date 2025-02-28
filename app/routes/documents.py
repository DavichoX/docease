from fastapi import APIRouter, Depends
from app.schemas.documents import DocumentCreate, Document
from app.services.users_service import get_current_user
from app.schemas.users import UserInDB
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.documents_services import create_document, get_document

documents = APIRouter()

@documents.post("/create", response_model=Document)
async def create_document_endpoint(document: DocumentCreate,
                                   db: AsyncSession = Depends(get_db),
                                   current: UserInDB = Depends(get_current_user)):
    document.created_by_id = current.id
    document.updated_by_id = current.id

    return await create_document(db=db, document=document)

@documents.get("/{document_id}", response_model=Document)
async def get_document_endpoint(document_id: int, db: AsyncSession = Depends(get_db)):
    document = get_document(document_id)
    return document


