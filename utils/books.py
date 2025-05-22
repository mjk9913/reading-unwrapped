from pydantic import BaseModel
from datetime import datetime

class Book(BaseModel):
    title: str
    author: str
    own_rating: float
    avg_rating: float
    num_pages: int
    pub_year: int
    read_date: datetime | None
    date_added: datetime | None
    rev: str | None
    read_count: int | None

