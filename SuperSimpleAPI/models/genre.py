import sys
sys.path.append('.')

from enum import Enum

class GenreEnum(Enum):
    """ Genres for Film model validation. """

    Action = "Action"
    Comedy = "Comedy"
    Drama = "Drama"
    Fantasy = "Fantasy"
    SciFi = "SciFi"
    Horror = "Horror"
    Thriller = "Thriller"