from fastapi import Body, FastAPI, HTTPException, status
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

# creating a method that allows one to fetch all books of a certain category
# the category is passed as a query parameter
@app.get("/books/")
def get_books_by_category(category: str):
    logger.info("returning all the books of category %s", category)
    books = [book for book in BOOKS if book["category"].casefold() == category.casefold()]
    return books

# creating a method that allows one to fetch all the books of a given author
# and then filter them out by Category as a querystring parameter
@app.get("/books/{author_name}/")
def get_books_by_author(author_name: str, category: str):
    logger.info("returning all the books of author %s in category %s", author_name, category)
    books = []
    for book in BOOKS:
        if  book["author"].casefold() == author_name.casefold() and \
            book["category"].casefold() == category.casefold():
            books.append(book)
    return books

# creating a method that allows one to add a new book to the existing list of books
# the body of the POST request should contain the book that will be added to the list
@app.post("/books", status_code=status.HTTP_201_CREATED)
def add_book(new_book=Body()):
    logger.info("adding a new book: %s", new_book)
    BOOKS.append(new_book) # TODO: This should be checked instead of blindly added to the list
    return BOOKS[-1]

# creating a method that allows one to update a book
# by sending it's new values, expect for the title, as the body
# of the PUT request
@app.put("/books", status_code=status.HTTP_202_ACCEPTED)
def update_book(updated_book=Body()):
    logger.info("updating book %s", updated_book)
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == updated_book["title"].casefold():
            BOOKS[i] = updated_book
            return BOOKS[i]
