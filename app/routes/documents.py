from fastapi import APIRouter, Depends
from app.schemas.documents import DocumentCreate, Document
from app.services.users_service import get_current_user
from app.schemas.users import UserInDB
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.documents_services import create_document, get_document, get_recent_documents, get_all_documents
from typing import List

documents = APIRouter()

@documents.post("/", response_model=Document)
async def create_document_endpoint(document: DocumentCreate,
                                   db: AsyncSession = Depends(get_db),
                                   current: UserInDB = Depends(get_current_user)):
    document.created_by_id = current.id
    document.updated_by_id = current.id

    return await create_document(db=db, document=document)


@documents.get("/recent", response_model=List[Document])
async def recent_documents(db: AsyncSession = Depends(get_db)):
    return await get_recent_documents(db)

@documents.get("/{document_id}", response_model=Document)
async def get_document_endpoint(document_id: int, db: AsyncSession = Depends(get_db)):
    document = await get_document(document_id,db)
    return document


@documents.get("/", response_model= List[Document])
async def all_documents(db: AsyncSession = Depends(get_db)):
    return await get_all_documents(db)


