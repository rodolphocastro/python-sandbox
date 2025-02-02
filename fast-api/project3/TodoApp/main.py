from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, Path
from dtos import CreateTodoDTO, TodosDTO
from database import engine, get_db
from models import Todos
from starlette import status
import models

app = FastAPI()
"""
our fastapi application
"""

# only executed if the db doesn't exist!
models.database.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]
"""
dependency injection hook for our database connection
"""

def __get_todo_by_id(db: Session, todo_id: int):
    """
    gets a todo by its id.
    Throws a 404 error if nothing is found.
    """
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {todo_id} wasn't found")
    return todo_model

@app.get("/todos", status_code=status.HTTP_200_OK, response_model=List[TodosDTO])
async def get_all_todos(db: db_dependency) -> List[Todos]:
    """
    gets all the to-dos currently in the system.
    """

    all_todos = db.query(Todos).all()
    return all_todos

@app.get("/todos/{todo_id}", status_code=status.HTTP_200_OK, response_model=TodosDTO)
async def get_todo(db: db_dependency,
                   todo_id: int = Path(gt=0)):
    """
    gets a single to-do based on its primary ID.
    """
    return __get_todo_by_id(db, todo_id)

@app.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency,
                      new_todo: CreateTodoDTO) -> int:
    """
    creates a new to-do.
    """
    todo = new_todo.to_Todos()
    db.add(todo)
    db.commit()
    return todo.id

@app.put("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def replace_todo(db: db_dependency,
                       updated_todo: CreateTodoDTO,
                       todo_id: int = Path(gt=0)):
    """
    replaces a todo's data with new data.
    """
    todo_model = __get_todo_by_id(db, todo_id)
    todo_model = updated_todo.apply_to_todos(todo_model)
    db.add(todo_model)
    db.commit()

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency,
                      todo_id: int = Path(gt=0)):
    """
    deletes a todo.
    """
    todo_model = __get_todo_by_id(db, todo_id)
    db.delete(todo_model)
    db.commit()
