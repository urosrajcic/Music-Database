from fastapi import HTTPException, Response, status
from app.genre.exceptions import *
from app.genre.services import GenreServices


class GenreController:
    @staticmethod
    def create_genre(name: str):
        try:
            genre = GenreServices.create_genre(name)
            return genre
        except GenreNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_genres_by_characters(characters: str):
        genres = GenreServices.get_genre_by_characters(characters)
        return genres

    @staticmethod
    def get_all_genres():
        genres = GenreServices.get_all_genres()
        return genres

    @staticmethod
    def delete_genre_by_name(name: str):
        try:
            GenreServices.delete_genre_by_name(name)
            return Response(content=f"Genre with provided name: {name} is deleted.")
        except GenreNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))
