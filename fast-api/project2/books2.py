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

BOOKS = [
    Book(1, "Computer Science Pro", "Doe, John", "A very nice book", 5),
    Book(2, "Be FAST with FastAPI", "Doe, John", "A great book", 5),
    Book(3, "Master endpoints", "Doe, John", "An awesome book", 5),
    Book(4, "HP1", "Author 1", "Book description", 2),
    Book(5, "HP2", "Author 2", "Book description", 3),
    Book(6, "HP3", "Author 3", "Book description", 1),
]

@app.get("/books")
async def get_all_books():
    """
    returns all the books currently in the system.
    """
    return BOOKS
