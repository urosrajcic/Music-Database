from fastapi import APIRouter, Depends

from app.album.schemas import *
from app.artist.controller import ArtistController
from app.artist.schemas import *
from app.group.schemas import GroupSchemaOut
from app.song.schemas import *
from app.user.controller import JWTBearer

artist_router = APIRouter(tags=["Artists"], prefix="/api/artists")


@artist_router.post("/add-new-artist", response_model=ArtistSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_artist(artist: ArtistSchemaIn):
    return ArtistController.create_artist(name=artist.name, country_name=artist.country_name,
                                          date_of_birth=artist.date_of_birth)


@artist_router.get("/get-artist-by-id", response_model=ArtistSchema)
def get_artist_by_id(id: str):
    return ArtistController.get_artist_by_id(id=id)


@artist_router.get("/get-artists-by-characters", response_model=list[ArtistSchemaOut])
def get_artists_by_characters(characters: str):
    return ArtistController.get_artist_by_characters(characters=characters)


@artist_router.get("/get-all-artists", response_model=list[ArtistSchemaOut])
def get_all_artists():
    return ArtistController.get_all_artists()


@artist_router.get("/get-artists-by-rating", response_model=list[ArtistSchemaOut])
def get_artists_by_rating():
    return ArtistController.get_artists_by_rating()


@artist_router.get("/get-artists-from-country", response_model=list[ArtistSchemaOut])
def get_artists_from_country(country: str):
    return ArtistController.get_artists_from_country(country=country)


@artist_router.get("/get-artist-with_most_awards", response_model=ArtistSchema)
def get_artist_with_most_awards():
    return ArtistController.get_artist_with_most_awards()


@artist_router.get("/get-artists-by-genre", response_model=list[ArtistSchemaOut])
def get_artists_by_genre(genre: str):
    return ArtistController.get_artist_by_genre(genre=genre)


@artist_router.get("/get-all-comments-about-artist")
def get_all_comments_about_artist(id: str):
    return ArtistController.get_all_comments_about_artist(id=id)


@artist_router.delete("/delete-artist-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_artist_by_id(id: str):
    return ArtistController.delete_artist_by_id(id=id)


@artist_router.put("/update-artist", response_model=ArtistSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_artist(artist: ArtistSchema):
    return ArtistController.update_artist(id=artist.id.__str__(), name=artist.name, date_of_birth=artist.date_of_birth,
                                          date_of_death=artist.date_of_death, vocalist=artist.vocalist,
                                          musician=artist.musician, producer=artist.producer, writer=artist.writer,
                                          engineer=artist.engineer, biography=artist.biography, ratings=artist.ratings,
                                          country_name=artist.country_name, record_label_id=artist.record_label_id)


@artist_router.put("/add-song-to-artist", response_model=ArtistSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_song_to_artist(artist: ArtistSchema, song: SongSchemaOut):
    return ArtistController.add_group_to_artist(artist_id=artist.id.__str__(), group_id=song.id.__str__())


@artist_router.put("/add-group-to-artist", response_model=ArtistSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_group_to_artist(artist: ArtistSchema, group: GroupSchemaOut):
    return ArtistController.add_group_to_artist(artist_id=artist.id.__str__(), group_id=group.id.__str__())


@artist_router.put("/add-album-to-artist", response_model=ArtistSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_album_to_artist(artist: ArtistSchema, album: AlbumSchemaOut):
    return ArtistController.add_album_to_artist(artist_id=artist.id.__str__(), album_id=album.id.__str__())


@artist_router.put("/add-award-to-artist", response_model=ArtistSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_award_to_artist(artist: ArtistSchema, award: AwardSchema):
    return ArtistController.add_award_to_artist(artist_id=artist.id.__str__(), award_id=award.id.__str__())


@artist_router.put("/add-genre-to-artist", response_model=ArtistSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_genre_to_artist(artist: ArtistSchema, genre: GenreSchema):
    return ArtistController.add_genre_to_artist(artist.id.__str__(), genre.name)


@artist_router.put("/add-comment-to-artist", response_model=ArtistSchema,
                   dependencies=[Depends(JWTBearer("classic_user"))])
def add_comment_to_artist(artist: ArtistSchema, comment: CommentSchema):
    return ArtistController.add_comment_to_artist(artist_id=artist.id.__str__(), comment_id=comment.id.__str__())


@artist_router.put("/remove-song-from-artist", response_model=ArtistSchema,
                   dependencies=[Depends(JWTBearer("super_user"))])
def remove_song_from_artist(artist: ArtistSchema, song: SongSchemaOut):
    return ArtistController.remove_group_from_artist(artist_id=artist.id.__str__(), group_id=song.id.__str__())


@artist_router.put("/remove-group-from-artist", response_model=ArtistSchema,
                   dependencies=[Depends(JWTBearer("super_user"))])
def remove_group_from_artist(artist: ArtistSchema, group: GroupSchemaOut):
    return ArtistController.remove_group_from_artist(artist_id=artist.id.__str__(), group_id=group.id.__str__())


@artist_router.put("/remove-album-from-artist", response_model=ArtistSchema,
                   dependencies=[Depends(JWTBearer("super_user"))])
def remove_album_from_artist(artist: ArtistSchema, album: AlbumSchemaOut):
    return ArtistController.remove_album_from_artist(artist_id=artist.id.__str__(), album_id=album.id.__str__())


@artist_router.put("/remove-award-from-artist", response_model=ArtistSchema,
                   dependencies=[Depends(JWTBearer("super_user"))])
def remove_award_from_artist(artist: ArtistSchema, award: AwardSchema):
    return ArtistController.remove_award_from_artist(artist_id=artist.id.__str__(), award_id=award.id.__str__())


@artist_router.put("/remove-genre-from-artist", response_model=ArtistSchema,
                   dependencies=[Depends(JWTBearer("super_user"))])
def remove_genre_from_artist(artist: ArtistSchema, genre: GenreSchema):
    return ArtistController.remove_genre_from_artist(artist_id=artist.id.__str__(), genre_name=genre.name)


@artist_router.put("/remove-comment-from-artist", response_model=ArtistSchema,
                   dependencies=[Depends(JWTBearer("super_user")), Depends(JWTBearer("classic_user")),
                                 Depends(JWTBearer("critic")), Depends(JWTBearer("writer"))])
def remove_comment_from_artist(artist: ArtistSchema, comment: CommentSchema):
    return ArtistController.remove_comment_from_artist(artist_id=artist.id.__str__(), comment_id=comment.id.__str__())
