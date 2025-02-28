from datetime import datetime
from optparse import Option

from pydantic import BaseModel
from typing import List, Optional
from app.schemas.blocks import BlockBase
from app.schemas.users import UserInDB

class DocumentBase(BaseModel):
    title: str
    created_by_id: int
    updated_by_id: Optional[int] = None

class DocumentCreate(DocumentBase):
    blocks: List[BlockBase]

class Document(DocumentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

