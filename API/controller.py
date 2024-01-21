from fastapi import APIRouter, HTTPException, Query, Depends
from bson import ObjectId
from models import Film, FilmPOST, FilmID
from logger import logger
from repository import FilmRepository

router = APIRouter()

"""Get all films."""
@router.get("/films", status_code=200, response_model=list[Film])
async def getAllFilms(limit: int = Query(10, description="Numbers of items to retrieve."), repository: FilmRepository = Depends()):
    try:
        result = repository.getAll(limit)
        if result is not None:
            return result
        else:
            raise HTTPException(status_code=404, detail="No films've been found.")
        
    except Exception as e:
        logger.error(f"[GET]Exception occured executing endpoint: {e}")
        raise HTTPException(status_code= 500, detail="Internal Server Error")

"""Get film by ID"""
@router.get("/films/{filmId}", response_model=Film)
async def getFilmById(filmId: ObjectId, repository: FilmRepository = Depends()):
    if(filmId is None):
        raise HTTPException(status_code=400, detail="Item ID cannot be null.")
    try:   
        result = repository.getByID(filmId)
        if result is not None:
            return result
        else:
            raise HTTPException(status_code=404, detail="Item not found.")
    except Exception as e:
        logger.error(f"[GET]Exception occured executing endpoint: {e}")
        raise HTTPException(status_code= 500, detail="Internal Server Error")

"""Add new film."""
@router.post("/films", status_code= 201, response_model= FilmID)
async def createNewFilm(film: FilmPOST, repository: FilmRepository = Depends()):
    try:
        created = repository.insert(film)
        return created
    except Exception as e:
        logger.error(f"[POST]Exception occured executing endpoint: {e}")
        raise HTTPException(status_code= 500, detail="Internal Server Error")
