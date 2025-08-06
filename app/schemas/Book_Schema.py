from enum import Enum
from typing import Optional

from pydantic import *

class ReadingStatus(str, Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    UNREAD = "unread"

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
    completed: Optional[str] = ReadingStatus.UNREAD
    # Rating
    rating: Optional[float] = None


class UpdateBook(BaseModel):
    # Book title
    title: Optional[str] = None
    # Author
    author: Optional[str] = None
    # publish date
    genre: Optional[str] = None
    # Genre
    year: Optional[int] = None
    # completed
    completed: Optional[str] = None
    # Rating
    rating: Optional[float] = None



