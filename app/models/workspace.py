from sqlalchemy import Integer, String, Boolean, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
from datetime import datetime

class Workspace(Base):
    __tablename__ = 'workspaces'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True),
                                                  server_default= func.now(),
                                                  autoincrement=False)