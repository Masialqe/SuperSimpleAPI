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
        #dev-only
        self.client = AsyncIOMotorClient("mongodb://localhost:2717/")
        #prod
        #self.client = AsyncIOMotorClient(f'mongodb://{os.environ.get("MONGO_DB","mongo_db")}:27017')
        self.db = self.client.FilmDB
        self.collection = self.db.filmCollection

    def __enter__(self):
        return self
    
    async def insert(self, newFilm: Film) -> str:
        """ Add new item to database"""
        result = await self.collection.insert_one(dict(newFilm))
        return str(result.inserted_id)
    
    async def getByID(self, filmID: str) -> dict:
        """ Retrieve item from DB by ID."""
        film = await self.collection.find_one({"_id": ObjectId(filmID)})
        if film is None:
            return None
        return individualMapper(film)
    
    async def getAll(self, limit: int) -> List[Film]:
        """ Retrieve all items from DB with limit."""
        cursor = self.collection.find().limit(limit)
        films = await cursor.to_list(length=limit)
        return serialMapper(films)
    
    async def deleteByID(self, filmID: str) -> bool:
        """ Delete item from DB"""
        result = await self.collection.delete_one({"_id" : ObjectId(filmID)})
        return result.deleted_count == 1
    
    async def updateByID(self, filmID: str, updatedFilm: Film) -> bool:
        """Update item by ID"""
        result = await self.collection.update_one({"_id": ObjectId(filmID)}, {"$set": dict(updatedFilm)})
        return result.modified_count > 0
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()

