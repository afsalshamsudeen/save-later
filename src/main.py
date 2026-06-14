from fastapi import FastAPI

from src.db.base import *
from src.db.database import Base, engine
from src.routes.bookmarks import router as bookmark_router
from src.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def root():
    return{"message" : "server up and running"}

app.include_router(bookmark_router)
app.include_router(auth_router)