def individualMapper(film) -> dict:
    """Map one object to dict"""
    return {
        "id": str(film["_id"]),
        "title": film["title"],
        "genre": film["genre"], 
        "releaseDate": film["releaseDate"],
        "director": film["director"]
    }

def serialMapper(films) -> list:
    """Map list of objects"""
    return [individualMapper(film) for film in films]