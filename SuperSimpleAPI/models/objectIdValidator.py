from bson import ObjectId
from fastapi import HTTPException, Depends
from repositories.filmRepository import FilmRepository

"""Validate given value if matches ObjectID """
def isValidObjectID(itemToValidate):
    try:
        ObjectId(itemToValidate)
        return True
    except Exception:
        return False
    
""" Validate object ID """
def ValidateObjectID(func):
    async def wrapper(filmID: str, repository: FilmRepository = Depends()):
        
        if not filmID:
            raise HTTPException(status_code=400, detail="Item ID cannot be null.")
        
        if not isValidObjectID(filmID):
            raise HTTPException(status_code=400, detail="ID should be a valid ObjectID.")
        
        return await func(filmID, repository)

    return wrapper
        