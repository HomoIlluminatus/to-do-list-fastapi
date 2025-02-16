from entities.entities import Category, User
from schemas.category_dto import CategoryResponse
from schemas.user_dto import UserDTO, UserResponse


def user_to_userdto(user: User) -> UserDTO:
    return UserDTO(**user.to_dict())


def userdto_to_user(user: UserDTO) -> User:
    return User(
        id=user.id,
        name=user.name,
        email=user.email,
        hashed_password=user.hashed_password,
        role=user.role,
        created_at=user.created_at,
        updated_at=user.updated_at
    )


def get_user_response(user: User) -> UserResponse:
    return UserResponse(
        id=user.id,
        name=user.name,
        email=user.email,
        role=user.role,
        created_at=user.created_at,
        updated_at=user.updated_at
    )
    

def get_category_response(category: Category) -> CategoryResponse:
    return CategoryResponse(
        id=category.id,
        title=category.title,
        description=category.description,
        created_at=category.created_at,
        updated_at=category.updated_at
    )
    