from typing import Self
from fastapi import FastAPI

app = FastAPI()

BOOKS = []

@app.get("/books")
async def get_all_books():
    """
    returns all the books currently in the system.
    """
    return BOOKS
