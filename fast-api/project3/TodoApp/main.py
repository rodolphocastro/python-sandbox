from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, Path
from dtos import CreateTodoDTO, TodosDTO
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

@app.get("/todos", status_code=status.HTTP_200_OK, response_model=List[TodosDTO])
async def get_all_todos(db: db_dependency) -> List[Todos]:
    """
    gets all the to-dos currently in the system.
    """

    all_todos = db.query(Todos).all()
    return all_todos

@app.get("/todos/{todo_id}", status_code=status.HTTP_200_OK, response_model=TodosDTO)
async def get_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    """
    gets a single to-do based on its primary ID.
    """
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"a TODO with id {todo_id} wasn't found")

@app.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, new_todo: CreateTodoDTO) -> int:
    """
    creates a new to-do.
    """
    todo = new_todo.to_Todos()
    db.add(todo)
    db.commit()
    return todo.id
