import sys
sys.path.append('.')

from pydantic import BaseModel, validator
from datetime import datetime
from models.genre import GenreEnum


class Film(BaseModel):
    """Base Film model class."""
    title: str 
    genre: str
    releaseDate: datetime
    director: str 

    #validate genre
    @validator("genre")
    def validateGenre(cls, value):
        if value not in [genre.value for genre in GenreEnum]:
            raise ValueError(f"Incorrect genre. Genre must be in {[genre.value for genre in GenreEnum]}")
        return value
    
 
class FilmResponse(BaseModel):
    """Film response model""" 
    id: str
    title: str 
    genre: str
    releaseDate: datetime
    director: str