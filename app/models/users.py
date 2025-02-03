from sqlalchemy import Integer, String, Boolean, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
from datetime import datetime

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, autoincrement=False)
    email: Mapped[str] = mapped_column(String, autoincrement=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String, autoincrement=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True),
                                                  server_default= func.now(),
                                                  autoincrement=False)

    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True),
                                                  server_default=func.now(),
                                                  default = datetime.now(),
                                                  onupdate= func.now(),
                                                  autoincrement=False)

