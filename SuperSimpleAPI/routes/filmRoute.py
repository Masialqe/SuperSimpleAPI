from fastapi import APIRouter, Depends, HTTPException, Query
from models.film import Film
from repositories.filmRepository import FilmRepository
from common.logger import logger
from bson import ObjectId


router = APIRouter()
"""Get all films endpoint"""
@router.get("/films", status_code= 200, response_model=list[Film])
async def GetAllFilms(limit: int = Query(10, description="Numbers of item to retrieve."),repository: FilmRepository = Depends()):
    try:
        result = repository.GetAll(limit)
        if result is not None:
            return result
        else:
            raise HTTPException(status_code=404, detail="Requested list is empty.")
    except Exception as ex:
        logger.error(f"[GET]: Exception occured executing endpoint: {ex}")
        raise HTTPException(status_code= 500, detail="Internal Server Error - failed to load entities.")

@router.get("/films/{filmID}", status_code= 200, response_model= Film)
async def GetFilmByID(filmID: str, repository: FilmRepository = Depends()):
    try:
        if filmID is None:
            raise HTTPException(status_code=400, detail="Item ID cannot be null.")
        result = repository.GetByID(filmID)
        if result is not None:
            return result
        else:
            raise HTTPException(status_code=404, detail="Item not found.")
    except Exception as ex:
        logger.error(f"[GET]: Exception occured executing endpoint: {ex}")
        raise HTTPException(status_code= 500, detail="Internal Server Error - failed to load entity.")

@router.post("/films", status_code= 201, response_model= ObjectId)
async def CreateNewFilm(newFilm: Film, repository: FilmRepository = Depends()):
    try:
        created = repository.Insert(newFilm)
        return created
    except Exception as ex:
        logger.error(f"[POST]: Exception occured executing endpoint: {ex}")
        raise HTTPException(status_code= 500, detail="Internal Server Error - failed to add new entity.")