from pydantic import BaseModel

class BlockBase(BaseModel):
    content: str
    order: int

class BlockCreate(BlockBase):
    doc_id: int
    created_by_id: int
    updated_by_id: int

class Block(BlockBase):
    id: int
    doc_id: int

    class Config:
        from_attributes = True