from pymongo import MongoClient
from models import FilmPOST, Film, FilmID
from bson import ObjectId

"""Film collection in mongo DB."""
class FilmRepository():

    def __enter__(self):
        self.mongoClient = MongoClient("localhost", 2717)
        self.mongoDatabase = self.MongoClient.FilmDB
        self.mongoCollection = self.mongoDatabase.Films

    """Insert new object """
    def insert(self, new_user: FilmPOST) -> FilmID:
        result = self.mongoCollection.insert_one(new_user.dict())
        return FilmID(id=ObjectId(str(result.inserted_id)))
    
    """Get object cy ID"""
    def getByID(self, ID: ObjectId) -> Film:
        result = self.mongoCollection.find_one({"_id": ID})
        return result
        
    """Get all object within limit"""
    def getAll(self, limit: int) -> list[Film]:
        cursor = self.mongoCollection.find().limit(limit)
        return [film for film in cursor]
        
    def __exit__(self):
        self.mongoClient.close()


        