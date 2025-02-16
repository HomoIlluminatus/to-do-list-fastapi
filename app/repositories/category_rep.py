from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from entities.entities import Category
from mappers.entities_models import (
    categorymodel_to_category,
    category_to_categorymodel
)
from models.models import CategoryModel
from .base_rep import AbstractBaseRepository


class AbstractCategoryRepository(AbstractBaseRepository[Category]):
    @abstractmethod
    async def get_user_categories_list(self, user_id: UUID) -> List[Category]:
        ...


class CategoryRepository(AbstractCategoryRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        
    async def get_by_id(self, category_id) -> Optional[Category]:
        queryset = await self._session.execute(
            select(CategoryModel).where(CategoryModel.id == category_id)
        )
        category = queryset.scalars().first()
        return categorymodel_to_category(category) if category else None
    
    async def get_list(self) -> List[Category]:
        queryset = await self._session.execute(select(CategoryModel))
        categories = queryset.scalars().all()
        return [categorymodel_to_category(category) for category in categories]
    
    async def get_user_categories_list(self, user_id: UUID) -> List[Category]:
        queryset = await self._session.execute(
            select(CategoryModel).where(CategoryModel.user_id == user_id)
        )
        categories = queryset.scalars().all()
        return [categorymodel_to_category(category) for category in categories]
    
    async def add(self, category: Category) -> Category:
        self._session.add(category_to_categorymodel(category))
        await self._session.commit()
        return category
    
    async def update(self, category: Category) -> Category:
        category_model = await self._session.merge(
            category_to_categorymodel(category)
        )
        await self._session.commit()
        category_model = await self._session.refresh(category_model)
        return categorymodel_to_category(category_model)
    
    async def delete(self, category_id) -> None:
        await self._session.execute(
            delete(CategoryModel).where(CategoryModel.id == category_id)
        )
    