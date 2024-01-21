from pydantic import BaseModel, validator, Field
from bson import ObjectId
from datetime import datetime
from enum import Enum

class GenreEnum(Enum):

    Action = "Action"
    Comedy = "Comedy"
    Drama = "Drama"
    Fantasy = "Fantasy"
    SciFi = "SciFi"
    Horror = "Horror"
    Thriller = "Thriller"

"""Film model"""
class Film(BaseModel):
    id: ObjectId = Field(alias="_id")
    title: str
    genre: str
    releaseDate: datetime
    director: str 
    addedToBase: datetime
    checksum: str

"""Create film model"""
class FilmPOST(BaseModel):
    title: str
    genre: str
    releaseDate: datetime
    director: str

    @validator("genre")
    def validateGenre(cls, value):
        if value not in [genre.value for genre in GenreEnum]:
            raise ValueError("Incorrect genre. Genre must be in [Action, Comedy, Drama, Fantasy, SciFi, Horror, Thriller]")
        return value
    
"""Return object ID."""
class FilmID(BaseModel):
    id: ObjectId = Field(alias="_id")