from fastapi import FastAPI, HTTPException
import logging

logger = logging.getLogger("uvicorn") # use the FastAPI (uvicorn) logger

logger.info("starting the FastAPI server...")
app = FastAPI() # instantiate the FastAPI class, which we'll be attaching methods to

logger.info("creating a few books")
BOOKS = [
    {"title": "Harry Potter", "author": "J.K. Rowling", "category": "fantasy"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "category": "fantasy"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "drama"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "category": "adventure"}
]

# creating a method that'll listen to GET requests on the / route of our server
@app.get("/books")
def get_all_books():
    logger.info("returning all the books")
    return BOOKS

# creating a method that allows one to fetch a book by its title.
# the title is passed as a path parameter in lieu of an id
# since we don't have an id field in our books
@app.get("/books/{title}")
def get_book_by_title(title: str):
    logger.info("returning the book with title %s", title)
    for book in BOOKS:
        if book["title"].casefold() == title.casefold():
            logger.info("found book: %s", book)
            return book
    logger.info("book not found")
    raise HTTPException(status_code=404, detail="Book not found")
