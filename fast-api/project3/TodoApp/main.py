from typing import Annotated, List
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

db_dependency = Annotated[Session, Depends(get_db)]
"""
dependency injection hook for our database connection
"""

@app.get("/todos")
async def get_all_todos(db: db_dependency):
    """
    gets all the TODOs currently in the system.
    """
    return db.query(Todos).all()
