from typing import Optional, Self
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

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

BOOKS: list[Book] = [
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

class BookPostRequest(BaseModel):
    """
    pydantic data model for POST'ing a book to the system.
    """
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=0, max_length=100)
    rating: int = Field(gt=0, lt=6)

def generate_book_id(book: Book) -> Book:
    """
    assigns an ID to a book based on the elements within then BOOKS collection.
    """
    # if there are books in the system find the last Book's ID and increment it
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        # otherwise this is the first book, its ID should be 1
        book.id = 1

    return book

@app.post("/books")
async def create_new_book(payload: BookPostRequest):
    """
    adds a new book to the system.
    """
    # important: on Pydantic >=3 this would be **payload.dict()
    book = Book(**payload.model_dump())
    BOOKS.append(generate_book_id(book))
