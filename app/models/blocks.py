from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
from app.models.documents import Documents
from datetime import datetime

class Block(Base):
    __tablename__ = 'blocks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content: Mapped[String] = mapped_column(String)
    doc_id: Mapped[int] = mapped_column(Integer, ForeignKey('Documents.id'))