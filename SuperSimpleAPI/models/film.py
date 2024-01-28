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
    
    #validate date
    @validator("releaseDate", pre=True, always=True)
    def validateReleaseDate(cls, value):
        if isinstance(value, datetime):
            return value
        try:
            return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        
        except ValueError:
            try:
                parsedIntoDatetime = datetime.strptime(value, "%Y-%m-%d").date()
                return datetime.combine(parsedIntoDatetime, datetime.min.time())
            
            except ValueError:
                raise ValueError("Input should be valid datetime format or regular date format (RRRR-MM-DD)")
        
class FilmResponse(Film):
    """Film response model""" 
    id: str
    