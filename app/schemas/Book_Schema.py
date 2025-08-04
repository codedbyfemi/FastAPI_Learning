from typing import Optional

from pydantic import *


class Book(BaseModel):
    # Book title
    title: str
    # Author
    author: str
    # publish date
    genre: str
    # Genre
    year: int
    # completed
    completed: Optional[bool] = False
    # Rating
    rating: Optional[float] = None
