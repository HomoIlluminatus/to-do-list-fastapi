from entities.entities import User
from schemas.user_dto import UserDTO, UserResponse


def user_to_userdto(user: User) -> UserDTO:
    return UserDTO(**user.user_dict)


def userdto_to_user(user: UserDTO) -> User:
    return User(**user.user_dict)

def get_user_response(user: User) -> UserResponse:
    return UserResponse(
        id=user.id,
        name=user.name,
        email=user.email,
        role=user.role,
        created_at=user.created_at,
        updated_at=user.updated_at
    )
    