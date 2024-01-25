import sys
sys.path.append('.')

from pydantic import BaseModel, validator
from datetime import datetime
from models.genre import GenreEnum

"""Base Film model class."""
class Film(BaseModel):

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
    
"""Film response model"""  
class FilmResponse(BaseModel):
    id: str
    title: str 
    genre: str
    releaseDate: datetime
    director: str