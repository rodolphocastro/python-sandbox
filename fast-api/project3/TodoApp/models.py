from database import database
from sqlalchemy import Column, Integer, String, Boolean

class Todos(database):
    """
    a model representing a To-Do object.
    """
    __tablename__ = "todos"

    """
    primary key column for our To-Do
    """
    id = Column(Integer, primary_key=True, index=True)

    """
    the name of our to-do
    """
    title = Column(String)

    """
    a brief description of our to-do
    """
    description = Column(String)

    """
    the priority of our to-do
    """
    priority = Column(Integer)

    """
    status of our to-do, if it is completed or not. Defaults to false (not completed)
    """
    complete = Column(Boolean, default=False)
