from typing import Self
from pydantic import BaseModel, Field
from models import Todos

class CreateTodoDTO(BaseModel):
    """
    a DTO (Data Transfer Object) to create a TODOs.
    """

    title: str = Field(min_length=3, max_length=100)
    description: str = Field(max_length=255)
    priority: int = Field(gt=0, lt=6)
    complete: bool = Field()

    def to_Todos(self: Self) -> Todos:
        """
        creates a new Todos instance using this instance's data.
        """
        return Todos(**self.model_dump())

    def apply_to_todos(self: Self, todo: Todos) -> Todos:
        """
        applies the data in this instance over to a Todos instance
        """
        todo.complete = self.complete
        todo.description = self.description
        todo.priority = self.priority
        todo.title = self.title
        return todo

class TodosDTO(BaseModel):
    """
    a DTO (Data Transfer Object) to report on TODOs.
    """

    id: int
    title: str
    description: str
    priority: int
    complete: bool
