from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime, UTC

from src.db.database import Base

class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    favicon = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda : datetime.now(UTC))
