from pymongo import MongoClient
from models import FilmPOST, Film, FilmID
from bson import ObjectId

"""Film collection in mongo DB."""
class FilmRepository():

    def __init__(self, host="localhost", port=2717, db_name="FilmDB", collection_name="Films"):
        self.mongoClient = MongoClient(host, port)
        self.mongoDatabase = self.mongoClient[db_name]
        self.mongoCollection = self.mongoDatabase[collection_name]

    def __enter__(self):
        return self
        #self.mongoClient = MongoClient("localhost", 2717)
        #self.mongoDatabase = self.mongoClientongoClient.FilmDB
        #self.mongoCollection = self.mongoDatabase.Films

    """Insert new object """
    def insert(self, new_user: FilmPOST) -> FilmID:
        result = self.mongoCollection.insert_one(new_user.dict())
        insertedID = str(result.inserted_id)
        if(insertedID):
            return FilmID(id=insertedID)
        else:
            raise ValueError("ID is null or empty.")
    
    """Get object cy ID"""
    def getByID(self, ID: str) -> Film:
        result = self.mongoCollection.find_one({"_id": ObjectId(ID)})
        return result
        
    """Get all object within limit"""
    def getAll(self, limit: int) -> list[Film]:
        cursor = self.mongoCollection.find().limit(limit)
        if cursor is None:
            return None
        return [Film(**film) for film in cursor]
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.mongoClient.close()


        