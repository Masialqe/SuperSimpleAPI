import sys
import os
sys.path.append('.')
from models.film import Film
from motor.motor_asyncio import AsyncIOMotorClient
from mappers.filmMapper import individualMapper, serialMapper
from bson import ObjectId
from typing import List
from datetime import datetime

""" CRUD operations for film collection"""
class FilmRepository():
    
    def __init__(self) -> None:
        #self.client = AsyncIOMotorClient("mongodb://localhost:2717/")
        self.client = AsyncIOMotorClient(f'mongodb://{os.environ.get("MONGO_DB","mongo_db")}:27017')
        self.db = self.client.FilmDB
        self.collection = self.db.filmCollection

    def __enter__(self):
        return self
    
    """ Add new item to database"""
    async def Insert(self, newFilm: Film) -> str:
        result = await self.collection.insert_one(dict(newFilm))
        return str(result.inserted_id)
    
    """ Retrieve item from DB by ID."""
    async def GetByID(self, filmID: str) -> dict:
        film = await self.collection.find_one({"_id": ObjectId(filmID)})
        if film is None:
            return None
        return individualMapper(film)
    
    """ Retrieve all items from DB with limit."""
    async def GetAll(self, limit: int) -> List[Film]:
        cursor = self.collection.find().limit(limit)
        films = await cursor.to_list(length=limit)
        return serialMapper(films)
    
    """ Delete item from DB"""
    async def DeleteByID(self, filmID: str) -> bool:
        result = await self.collection.delete_one({"_id" : ObjectId(filmID)})
        return result.deleted_count == 1
    
    """Update item by ID"""
    async def UpdateByID(self, filmID: str, updatedFilm: Film) -> bool:
        result = await self.collection.update_one({"_id": ObjectId(filmID)}, {"$set": dict(updatedFilm)})
        return result.modified_count > 0
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()

