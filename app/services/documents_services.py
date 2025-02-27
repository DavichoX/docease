from fastapi import HTTPException, status
from alembic.util import status
from sqlalchemy import select
from app.models.documents import Documents
from app.models.blocks import Block
from app.schemas.documents import Document, DocumentCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def create_document(document: DocumentCreate, db: AsyncSession):
    db_document = Document(
        title=document.title,
        created_by_id=document.created_by_id,
        updated_by_id=document.updated_by_id,
    )
    db.add(db_document)
    await db.commit()
    await db.refresh(db_document)

    for block in document.blocks:
        db_block = Block(
            content = block.content,
            order = block.order,
            doc_id = db_document.id,
            created_by_id=db_document.created_by_id,
            updated_by_id=db_document.updated_by_id,
        )
        db.add(db_block)
        await db.commit()
        return db_document

async def get_document(document_id: int,db: AsyncSession):
    result = await db.execute(select(Documents).where(Documents.id == document_id))
    document = result.scalar_one_or_none()
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return document

async def delete_document():
    pass