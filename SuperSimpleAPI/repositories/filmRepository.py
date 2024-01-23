from models.film import Film
from pymongo import MongoClient
from mappers.filmMapper import individualMapper, serialMapper
from bson import ObjectId


from datetime import datetime

class FilmRepository():
    
    def __init__(self) -> None:
        self.client = MongoClient("localhost", 2717)
        self.db = self.client.FilmDB
        self.collection = self.db.filmCollection

    def __enter__(self):
        return self
    
    def test(self):
        try:
            self.client.admin.command("ping")
            print(" I can ping!!")
        except Exception as e:
            print(e)
    """ Add new item to database"""
    def Insert(self, newFilm: Film) -> ObjectId:
        result = self.collection.insert_one(dict(newFilm))
        return result.inserted_id
    
    """ Retrieve item from DB by ID."""
    def GetByID(self, filmID: str) -> dict:
        film = self.collection.find_one({"_id": ObjectId(filmID)})
        return individualMapper(film)
    
    """ Retrieve all items from DB with limit."""
    def GetAll(self, limit) -> list[Film]:
        films = self.collection.find().limit(limit)
        return [Film(**film) for film in films]
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()


with FilmRepository() as repo:
    film = {
        "title": "title",
        "genre": "Drama", 
        "releaseDate": datetime.now,
        "director": "director"
    }

    result = repo.insert(film)
    print(result)


