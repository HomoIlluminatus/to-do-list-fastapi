from entities.entities import User
from schemas.user_dto import UserDTO


def user_to_userdto(user: User) -> UserDTO:
    return UserDTO(**user.user_dict)


def userdto_to_user(user: UserDTO) -> User:
    return User(**user.user_dict)