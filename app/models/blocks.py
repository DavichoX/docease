from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
from app.models.documents import Documents
from datetime import datetime

class Block(Base):
    __tablename__ = 'blocks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content: Mapped[String] = mapped_column(String)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True),
                                                  server_default = func.now(),
                                                  autoincrement=False)
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True),
                                                  server_default = func.now(),
                                                  default = datetime.now(),
                                                  onupdate=func.now(),
                                                  autoincrement=False)
    order: Mapped[int] = mapped_column(Integer)
    doc_id: Mapped[int] = mapped_column(Integer, ForeignKey('documents.id'))
    created_by_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    updated_by_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))