from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from database import engine, local_session
from models import Todos
import models

app = FastAPI()
"""
our fastapi application
"""

# only executed if the db doesn't exist!
models.database.metadata.create_all(bind=engine)

def get_db():
    """
    gets a working local session of our database.
    it automatically closes the database connection once done.
    """
    db = local_session()
    try:
        # yield is a type of return with extra logic to handle doing something after it is finished.ß
        yield db
    finally:
        db.close()

@app.get("/todos")
async def get_all_todos(db: Annotated[Session, Depends(get_db)]):
    """
    gets all the TODOs currently in the system.
    """
    return db.query(Todos).all()
