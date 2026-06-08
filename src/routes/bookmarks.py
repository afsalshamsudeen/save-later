from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.database import get_db

from src.schemas.bookmarkschema import(
    BookmarkCreate,
    BookmarkResponse
)

from src.services.bookmark_services import(
    create_bookmark,
    get_all_bookmark,
    delete_bookmark
)

router = APIRouter(
    prefix="/bookmarks",
    tags=["Bookmarks"]
)


@router.post("/", response_model=BookmarkResponse)
def add_bookmark(bookmark: BookmarkCreate, db: Session = Depends(get_db)):
    return create_bookmark(db, bookmark)

@router.get("/", response_model=list[BookmarkResponse])
def fetch_bookmarks(db: Session = Depends(get_db)):
    return get_all_bookmark(db)

@router.delete("/{bookmark_id}")
def remove_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    deleted = delete_bookmark(db, bookmark_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Bookmark Not Found!"

        )
    return {
        "message": "Bookmark deleted successfully!"
    } 