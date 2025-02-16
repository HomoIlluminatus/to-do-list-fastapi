from abc import abstractmethod
from typing import List, Optional
from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from entities.entities import User
from models.models import UserModel
from mappers.entities_models import usermodel_to_user, user_to_usermodel
from .base_rep import AbstractBaseRepository


class AbstractUserRepository(AbstractBaseRepository[User]):
    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[User]:
        ...
    

class UserRepository(AbstractUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
           
    async def get_by_id(self, user_id: UUID) -> Optional[User]:
        queryset = await self._session.execute(
            select(UserModel).where(UserModel.id == user_id)
        )
        user_model = queryset.scalars().first()
        return usermodel_to_user(user_model) if user_model else None
    
    async def get_by_email(self, email: str) -> Optional[User]:
        queryset = await self._session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        user_model = queryset.scalars().first()
        return usermodel_to_user(user_model) if user_model else None
    
    async def get_list(self) -> List[User]:
        queryset = await self._session.execute(select(UserModel))
        return [usermodel_to_user(user) for user in queryset.scalars().all()]
    
    async def add(self, user: User) -> User:
        self._session.add(user_to_usermodel(user))
        await self._session.commit()
        return user
    
    async def update(self, user: User) -> User:
        user_model = await self._session.merge(user_to_usermodel(user))
        await self._session.commit()
        await self._session.refresh(user_model)
        return usermodel_to_user(user_model)
        
    async def delete(self, user_id) -> None:
        await self._session.execute(
            delete(UserModel).where(UserModel.id == user_id)
        )
        await self._session.commit()  
        