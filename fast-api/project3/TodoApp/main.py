from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from database import engine, local_session
from models import Todos
from starlette import status
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

@app.get("/todos/{todo_id}")
async def get_todo(db: db_dependency, todo_id: int):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"a TODO with id {todo_id} wasn't found")
