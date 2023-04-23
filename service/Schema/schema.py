from pydantic import BaseModel
from typing import List

class MovieSchema(BaseModel):
    title: str
    keywords: List[str] = []
    director: str
    year: int