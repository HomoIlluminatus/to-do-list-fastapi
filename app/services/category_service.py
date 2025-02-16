from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from core.errors.category_error import CategoryNotFoundError
from entities.entities import Category
from repositories.category_rep import AbstractCategoryRepository


class AbstractCategoryService(ABC):
    @abstractmethod
    async def get_category_or_raise(self, category_id: UUID) -> Category:
        ...
        
    @abstractmethod
    async def get_categories_list(self) -> List[Category]:
        ...
    
    @abstractmethod
    async def get_user_categories_list(self, user_id: UUID) -> List[Category]:
        ...
    
    @abstractmethod
    async def create_category(self, user_id: UUID, title:str,
                              description: Optional[str]=None) -> Category:
        ...
        
    @abstractmethod
    async def update_category(self, category: Category) -> Category:
        ...
    
    @abstractmethod
    async def delete_category(self, category_id: UUID) -> None:
        ...
        

class CategoryService(AbstractCategoryService):
    def __init__(self, category_rep: AbstractCategoryRepository) -> None:
        self._category_rep = category_rep
        
    async def get_category_or_raise(self, category_id: UUID) -> Category:
        category = await self._category_rep.get_by_id(category_id)
        if category is None:
            raise CategoryNotFoundError(category_id)
        return category
    
    async def get_categories_list(self) -> List[Category]:
        return await self._category_rep.get_list()
    
    async def get_user_categories_list(self, user_id: UUID) -> List[Category]:
        return await self._category_rep.get_user_categories_list(user_id)
    
    async def create_category(self, user_id: UUID, title: str,
                              description: Optional[str] = None) -> Category:
        return await self._category_rep.add(
            Category(user_id=user_id, title=title, description=description)
        )
        
    async def update_category(self, category: Category) -> Category:
        return await self._category_rep.update(category)
    
    async def delete_category(self, category_id: UUID) -> None:
        await self._category_rep.delete(category_id)
        