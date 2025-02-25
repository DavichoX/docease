from sqlalchemy import Integer, String, Boolean, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
from datetime import datetime
from app.models.users import Users
class WorkspaceSettings(Base):
    __tablename__ = 'workspace_settings'

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    theme: Mapped[str] = mapped_column(String, default="light")
    color: Mapped[str] = mapped_column(String, default="green")
    font_size:Mapped[int] = mapped_column(Integer, default=16)

    user = relationship('Users', back_populates='workspace_settings')