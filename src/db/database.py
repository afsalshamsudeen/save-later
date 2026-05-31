# creates connection between fastapi and postgresql
from sqlalchemy import create_engine
# session maintain a temporary conversation between batabase, helps to create, update, delete, query.
# declerative base create base class for models, every model inherit from base
from sqlalchemy.orm import sessionmaker, declarative_base
#importing DB URL  from config file
from src.core.config import DATABASE_URL
# This create actuall database connection
engine = create_engine(DATABASE_URL)

# creates session factory ,means every requests creates its own DB session
# autocommit=False: prevent db to save automatic, each action will be saved manuelly which is good
# autoflush = False : Prevents automatic syncing
sessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

# Dependancy
def get_db():
    # create DB session per request
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
