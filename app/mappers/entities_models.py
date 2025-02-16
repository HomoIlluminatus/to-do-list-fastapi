from entities.entities import User, Category, Task
from models.models import UserModel, CategoryModel, TaskModel


def user_to_usermodel(user: User) -> UserModel:
    return UserModel(
        id=user.id,
        name=user.name,
        email=user.email,
        hashed_password=user.hashed_password,
        role=user.role,
        created_at=user.created_at,
        updated_at=user.updated_at
    )


def usermodel_to_user(user: UserModel) -> User:
    return User(
        id=user.id,
        name=user.name,
        email=user.email,
        hashed_password=user.hashed_password,
        role=user.role,
        created_at=user.created_at,
        updated_at=user.updated_at     
    )
    

def category_to_categorymodel(category: Category) -> CategoryModel:
    return CategoryModel(**category.to_dict())


def categorymodel_to_category(category: CategoryModel) -> Category:
    return Category(
        id=category.id,
        user_id=category.user_id,
        title=category.title,
        description=category.description,
        created_at=category.created_at,
        updated_at=category.updated_at
    )
    