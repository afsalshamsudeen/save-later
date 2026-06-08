from sqlalchemy.orm import Session

from src.models.bookmark import Bookmark
from src.schemas.bookmarkschema import BookmarkCreate

def create_bookmark(db: Session, bookmark: BookmarkCreate):

    # Create SQLAlchemy  object
    new_bookmark = Bookmark(
        url = bookmark.url,
        title = bookmark.title,
        favicon = bookmark.favicon
    )
    #Not save yet, adding to session
    db.add(new_bookmark)
    # save to postgresql
    db.commit()
    # reload object from  DB. why important? Maybe DB generate timestamp or id so...
    db.refresh(new_bookmark)

    return new_bookmark


def get_all_bookmark(db: Session):

    return db.query(Bookmark).all()


def delete_bookmark(db: Session, bookmark_id: int):

    bookmark = db.query(Bookmark).filter(
        Bookmark.id == bookmark_id
    ).first()

    if not bookmark:
        return None
    
    # marks row for deleting
    db.delete(bookmark)
    # delete permenantly
    db.commit()

    return bookmark