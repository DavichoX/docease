from app.models.documents import Documents
from app.models.blocks import Block
from app.schemas.blocks import Block, BlockCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def create_block(block: BlockCreate, db:AsyncSession):
    db_block = Block(**block.model_dump())
    db.add(db_block)
    await db.commit()
    await db.refresh(db_block)
    return db_block