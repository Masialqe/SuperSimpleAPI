"""Map one object to dict"""
def individualMapper(film) -> dict:
    return {
        "id": str(film["_id"]),
        "title": film["name"],
        "genre": film["genre"], 
        "releaseDate": film["releaseDate"],
        "director": film["director"]
    }

"""Map list of objects"""
def serialMapper(films) -> list:
    return [individualMapper(film) for film in films]