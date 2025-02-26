from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
from app.models.documents import Documents
from datetime import datetime

class Collaboration(Base):
    __tablename__ = 'collaboration'

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("Users.id") , primary_key=True)
