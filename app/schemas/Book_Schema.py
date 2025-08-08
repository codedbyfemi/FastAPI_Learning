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
    rating: Optional[float] = Field(le=5)


class UpdateReadingStatus(BaseModel):
    # completed
    completed: ReadingStatus

class SetRating(BaseModel):
    # rating
    rating: float = Field(le=5)



