from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import *

from app.schemas.Book_Schema import Book

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
async def create_book(book: Book = Body(...), response: Response = Response()):
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
    response.status_code = status.HTTP_201_CREATED
    return {
        "response": {
            "Book Details": books[-1],
       }
   }

@app.get("/books")
async def read_books(response: Response):
    response.status_code = status.HTTP_200_OK
    return books

@app.get("/books/{book_id}")
async def read_book(book_id: int, response: Response):
    book = books[book_id - 1]
    response.status_code = status.HTTP_200_OK
    return Book(**book)

@app.delete("/books/{book_id}")
async def delete_book(book_id: int, response: Response):
    for n in books:
        if n["id"] == book_id:
            books.remove(n)
            response.status_code = status.HTTP_204_NO_CONTENT
            return None
    response.status_code = status.HTTP_404_NOT_FOUND
    return HTTPException(status_code=404, detail="Book not found")

@app.delete("/books")
async def delete_books(response: Response):
    books.clear()
    response.status_code = status.HTTP_204_NO_CONTENT
    return None

@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book, response: Response):
    for n in books:
        if n["id"] == book_id:
            n.update(book)
            response.status_code = status.HTTP_200_OK
            return Book(**n)

    response.status_code = status.HTTP_404_NOT_FOUND
    return HTTPException(status_code=404, detail="Book not found")
