from fastapi import APIRouter, Depends, HTTPException, Query
from models.film import Film, FilmResponse
from models.objectIDValidator import validateObjectID, isValidObjectID
from repositories.filmRepository import FilmRepository
from common.logger import logger

router = APIRouter()

@router.get("/films", status_code= 200, response_model=list[FilmResponse])
async def getAllFilms(limit: int = Query(10, description="Numbers of item to retrieve."),repository: FilmRepository = Depends()):
    """Get all films """
    try:
        result = await repository.GetAll(limit)
        if not result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Requested list is empty.")
        
    except HTTPException as httpEx:
            raise httpEx
    
    except Exception as ex:
        logger.error(f"[GET]: Exception occured executing endpoint (films): {ex}")
        raise HTTPException(status_code= 500, detail="Internal Server Error - failed to load entities.")

@router.get("/films/{filmID}", status_code= 200, response_model= FilmResponse)
@validateObjectID
async def getFilmByID(filmID: str, repository: FilmRepository = Depends()):
        """Get one film by ID """
        try:
            result = await repository.getByID(filmID)
            if result is not None:
                return result
            else:
                raise HTTPException(status_code=404, detail="Item not found.")
            
        except HTTPException as httpEx:
            raise httpEx
        
        except Exception as ex:
            logger.error(f"[GET]: Exception occured executing endpoint (films/ID): {ex}")
            raise HTTPException(status_code= 500, detail="Internal Server Error - failed to load entity.")

@router.post("/films", status_code= 201, response_model= str)
async def createNewFilm(newFilm: Film, repository: FilmRepository = Depends()):
    """Create new film """
    try:
        created = await repository.insert(newFilm)
        return created
    
    except Exception as ex:
        logger.error(f"[POST]: Exception occured executing endpoint: {ex}")
        raise HTTPException(status_code= 500, detail="Internal Server Error - failed to add new entity.")
    
@router.delete("/films/{filmID}", status_code=204)
@validateObjectID
async def deleteExistingFilm(filmID: str, repository: FilmRepository = Depends()):
    """Delete film """
    try:
        result = await repository.deleteByID(filmID)
        if not result:
            raise HTTPException(status_code=404, detail="Item not found.")
             
    except HTTPException as httpEx:
            raise httpEx
    
    except Exception as ex:
        logger.error(f"[DELETE]: Exception occured executing endpoint (films/ID): {ex}")
        raise HTTPException(status_code= 500, detail="Internal Server Error - failed to delete entity.")
    
@router.put("/films/{filmID}", status_code= 204)

#@validateObjectID
async def updateExistingFilm(filmID: str, updatedFilm: Film, repository: FilmRepository = Depends()):
    """ Update existing film by ID """
    try:
        if not isValidObjectID(filmID):
            raise HTTPException(status_code=400, detail="ID Should be valid ObjectID.")
        else:
             result = await repository.updateByID(filmID, updatedFilm)
             if not result:
                  raise HTTPException(status_code=404, detail="Item not found.")
             
    except HTTPException as httpEx:
            raise httpEx
    
    except Exception as ex:
        logger.error(f"[PUT]: Exception occured executing endpoint (films/ID): {ex}")
        raise HTTPException(status_code= 500, detail="Internal Server Error - failed to update entity.")
     

    