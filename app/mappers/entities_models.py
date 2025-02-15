from entities.entities import User
from models.models import UserModel


def user_to_usermodel(user: User) -> UserModel:
    return UserModel(**user.user_dict)


def usermodel_to_user(user: UserModel) -> User:
    return User(**user.user_dict)
