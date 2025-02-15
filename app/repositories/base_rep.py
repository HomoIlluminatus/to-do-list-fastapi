from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic
from uuid import UUID


T = TypeVar("T")


class AbstractBaseRepository(ABC, Generic[T]):
    @abstractmethod
    async def get_by_id(self, entity_id: UUID) -> T:
        ...
        
    @abstractmethod
    async def get_list(self) -> List[T]:
        ...
    
    @abstractmethod
    async def add(self, entity: T) -> T:
        ...
    
    @abstractmethod
    async def update(self, entity: T) -> T:
        ...
        
    @abstractmethod
    async def delete(self, entity_id: UUID) -> None:
        ...
        