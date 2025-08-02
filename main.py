from operator import indexOf

from fastapi import FastAPI, HTTPException
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

    for n in books:
        if n["title"] == book.title and n["author"] == book.author and n["genre"] == book.genre and n["year"] == book.year:
            return HTTPException(status_code=404, detail="Book already exists")

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
            "Book Details": books[-1],
       }
   }

@app.get("/books")
async def read_books():
    return books

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    book = books[book_id - 1]
    return Book(**book)

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for n in books:
        if n["id"] == book_id:
            books.remove(n)
            return books
    return HTTPException(status_code=404, detail="Book not found")

