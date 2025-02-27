from sqlalchemy import Integer, String, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
from app.models.users import Users
from datetime import datetime

class Documents(Base):
    __tablename__ = 'documents'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True),
                                                  server_default=func.now(),
                                                  autoincrement=False)
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True),
                                                 server_default=func.now(),
                                                 default = datetime.now(),
                                                 onupdate=func.now,
                                                 autoincrement=False)
    created_by_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    updated_by_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))