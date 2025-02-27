from datetime import datetime
from pydantic import BaseModel
from typing import List
from app.schemas.blocks import BlockBase

class DocumentBase(BaseModel):
    title: str
    created_by_id: int
    updated_by_id: int

class DocumentCreate(DocumentBase):
    blocks: List[BlockBase]

class Document(DocumentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

