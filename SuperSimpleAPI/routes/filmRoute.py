from fastapi import APIRouter, Depends, HTTPException, Query
from models.film import Film, FilmResponse
import models.objectIdValidator as objectIdValidator
from repositories.filmRepository import FilmRepository
from common.logger import logger

router = APIRouter()

"""Get all films endpoint"""
@router.get("/films", status_code= 200, response_model=list[FilmResponse])
async def GetAllFilms(limit: int = Query(10, description="Numbers of item to retrieve."),repository: FilmRepository = Depends()):
    try:
        result = await repository.GetAll(limit)
        if result is not None:
            return result
        else:
            raise HTTPException(status_code=404, detail="Requested list is empty.")
        
    except HTTPException as httpEx:
            raise httpEx
    
    except Exception as ex:
        logger.error(f"[GET]: Exception occured executing endpoint (films): {ex}")
        raise HTTPException(status_code= 500, detail="Internal Server Error - failed to load entities.")

"""Get one film by ID endpoint"""
@router.get("/films/{filmID}", status_code= 200, response_model= FilmResponse)
@objectIdValidator.ValidateObjectID
async def GetFilmByID(filmID: str, repository: FilmRepository = Depends()):
        try:
            result = await repository.GetByID(filmID)
            if result is not None:
                return result
            else:
                raise HTTPException(status_code=404, detail="Item not found.")
            
        except HTTPException as httpEx:
            raise httpEx
        
        except Exception as ex:
            logger.error(f"[GET]: Exception occured executing endpoint (films/ID): {ex}")
            raise HTTPException(status_code= 500, detail="Internal Server Error - failed to load entity.")

"""Create new film endpoint"""
@router.post("/films", status_code= 201, response_model= str)
async def CreateNewFilm(newFilm: Film, repository: FilmRepository = Depends()):
    try:
        created = await repository.Insert(newFilm)
        return created
    
    except Exception as ex:
        logger.error(f"[POST]: Exception occured executing endpoint: {ex}")
        raise HTTPException(status_code= 500, detail="Internal Server Error - failed to add new entity.")
    
"""Delete film endpoint """
@router.delete("/films/{filmID}", status_code=204)
@objectIdValidator.ValidateObjectID
async def DeleteExistingFilm(filmID: str, repository: FilmRepository = Depends()):
    try:
        result = await repository.DeleteByID(filmID)
        if not result:
            raise HTTPException(status_code=404, detail="Item not found.")
             
    except HTTPException as httpEx:
            raise httpEx
    
    except Exception as ex:
        logger.error(f"[DELETE]: Exception occured executing endpoint (films/ID): {ex}")
        raise HTTPException(status_code= 500, detail="Internal Server Error - failed to delete entity.")
    
""" Update existing film by ID endpoint"""
@router.put("/films/{filmID}", status_code= 204)
#@objectIdValidator.ValidateObjectID
async def UpdateExistingFilm(filmID: str, updatedFilm: Film, repository: FilmRepository = Depends()):
    try:
        if not objectIdValidator.IsValidObjectID(filmID):
            raise HTTPException(status_code=400, detail="ID Should be valid ObjectID.")
        else:
             result = await repository.UpdateByID(filmID, updatedFilm)
             if not result:
                  raise HTTPException(status_code=404, detail="Item not found.")
             
    except HTTPException as httpEx:
            raise httpEx
    
    except Exception as ex:
        logger.error(f"[PUT]: Exception occured executing endpoint (films/ID): {ex}")
        raise HTTPException(status_code= 500, detail="Internal Server Error - failed to update entity.")
     

    