from fastapi import FastAPI
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
def all_books():
    logger.info("returning all the books")
    return BOOKS
