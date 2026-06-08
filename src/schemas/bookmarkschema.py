from pydantic import BaseModel
from datetime import datetime

# This validates incoming request body
class BookmarkCreate(BaseModel):
    url : str
    title : str | None = None
    favicon : str | None = None

# Defines API response format
class BookmarkResponse(BaseModel):
    id: int
    url: str 
    title: str | None
    favicon: str | None
    created_at: datetime


    class Config:
    # This allows pydantic to convert SQLAlchemy object to JSON response
        from_attributes = True