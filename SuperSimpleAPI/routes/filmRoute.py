from fastapi import APIRouter
#from repositories.filmRepository import FilmRepository

router = APIRouter()

@router.get("/films", status_code= 200)
def GetAllFilms():
    return {}