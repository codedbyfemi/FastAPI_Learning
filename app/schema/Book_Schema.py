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
    # Rating
    rating: Optional[float] = None