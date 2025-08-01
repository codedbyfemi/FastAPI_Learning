from fastapi import FastAPI
from fastapi.params import *

from app.schema.Book_Schema import Book

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The British sports",
        "author": "<NAME>",
        "genre": "Sci-Fi",
        "year": 2000,
        "rating": 4.5,

    }
]

@app.post("/books")
async def create_book(book: Book = Body(...)):
    book.model_dump()
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "year": book.year,
        "rating": book.rating,
    }
    books.append(new_book)
    return {
        "response": {
            "Book Details": Book(**new_book).model_dump(),
       }
   }

@app.get("/books")
async def read_books():
    return books

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    book = books[book_id - 1]
    return Book(**book)