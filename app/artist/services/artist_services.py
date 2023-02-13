from app.db.database import SessionLocal
from app.artist.repository.artist_repository import ArtistRepository


class ArtistServices:
    @staticmethod
    def create_artist(name: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.create_artist(name)
        except Exception as e:
            raise e

    @staticmethod
    def get_artist_by_id(id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_artist_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def get_artist_by_name(name: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_artists_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_artists():
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_all_artists()
        except Exception as e:
            raise e

    @staticmethod
    def delete_artist_by_id(id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.delete_artis_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def update_artist(id: str, name=None, date_of_birth=None, date_of_death=None, ratings=None, vocalist=None,
                      musician=None, producer=None, writer=None, engineer=None, biography=None, album_id=None,
                      song_id=None, genre_name=None, award_id=None, country_name=None, user_username=None,
                      record_label_id=None):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.update_artist(id, name, date_of_birth, date_of_death, ratings, vocalist,
                                                       musician, producer, writer, engineer, biography, album_id,
                                                       song_id, genre_name, award_id, country_name, user_username,
                                                       record_label_id)
        except Exception as e:
            raise e