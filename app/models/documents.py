from sqlalchemy import Integer, String, TIMESTAMP, func
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
    user_id: Mapped[int] = mapped_column(Integer, foreign_key='Users.id')