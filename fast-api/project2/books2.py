from typing import Self
from fastapi import FastAPI

class Book:
    """
    represents a physical book in our API.
    """

    def __init__(self, id: int, title: str, author: str, description: str, rating: int) -> Self:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

app = FastAPI()

BOOKS = []

@app.get("/books")
async def get_all_books():
    """
    returns all the books currently in the system.
    """
    return BOOKS
