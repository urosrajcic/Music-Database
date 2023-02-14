from fastapi import APIRouter
from app.user.controller import UserController
from app.user.schemas import *

user_router = APIRouter(tags=["users"], prefix="/mdb/users")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.username, user.email, user.password, user.name, user.surname,
                                      user.date_of_birth, user.country_name)


@user_router.post("/add-new-critic", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_critic(user.username, user.email, user.password, user.name, user.surname,
                                        user.date_of_birth, user.country_name)


@user_router.post("/add-new-writer", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_writer(user.username, user.email, user.password, user.name, user.surname,
                                        user.date_of_birth, user.country_name)


@user_router.post("/add-new-critic-and_writer", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_writer_and_critic(user.username, user.email, user.password, user.name, user.surname,
                                                   user.date_of_birth, user.country_name)


@user_router.get("/get-user-by-username", response_model=UserSchema)
def get_user_by_username(username: str):
    return UserController.get_user_by_username(username)


@user_router.get("/get-user-by-email", response_model=UserSchema)
def get_user_by_email(email: str):
    return UserController.get_user_by_email(email)


@user_router.get("/get-user-by-characters", response_model=list[UserSchema])
def get_users_by_characters(characters: str):
    return UserController.get_users_by_characters(characters)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all_users()


@user_router.delete("/delete-user-by-username")
def delete_user_by_username(username: str):
    return UserController.delete_user_by_username(username)


@user_router.put("/update-user-by-username", response_model=UserSchema)
def update_user(username: str, password: str = None, name: str = None,
                surname: str = None, country_name: str = None):
    return UserController.update_user(username, password, name, surname, country_name)