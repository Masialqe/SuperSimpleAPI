from bson import ObjectId
from fastapi import HTTPException, Depends
from repositories.filmRepository import FilmRepository
from functools import wraps

def isValidObjectID(itemToValidate):
    """Validate given value if matches ObjectID """
    try:
        ObjectId(itemToValidate)
        return True
    except Exception:
        return False
    

def validateObjectID(func):
    """ Validate object ID """
    @wraps(func)
    async def wrapper(filmID: str, 
                      repository: FilmRepository = Depends(),
                      *args, 
                      **kwargs):
        
        if not filmID:
            raise HTTPException(status_code=400, detail="Item ID cannot be null.")
        
        if not isValidObjectID(filmID):
            raise HTTPException(status_code=400, detail="ID should be a valid ObjectID.")
        
        return await func(filmID, repository=repository, *args, **kwargs)

    return wrapper