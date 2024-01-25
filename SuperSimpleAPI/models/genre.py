import sys
sys.path.append('.')

from enum import Enum

""" Genres for Film model validation. """
class GenreEnum(Enum):

    Action = "Action"
    Comedy = "Comedy"
    Drama = "Drama"
    Fantasy = "Fantasy"
    SciFi = "SciFi"
    Horror = "Horror"
    Thriller = "Thriller"