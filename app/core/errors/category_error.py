from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from .base_error import BaseAppError


@dataclass
class CategoryError(BaseAppError):
    @property
    def message(self) -> str:
        return 'Category error'


@dataclass
class CategoryNotFoundError(CategoryError):
    category_id: Optional[UUID]
    
    @property
    def message(self) -> str:
        if self.category_id is None:
            return 'Category not found'
        return f'Category not found: id {self.category_id}'
    