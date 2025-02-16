from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from core.errors.user_error import UserNotFoundError
from entities.entities import User
from entities.utils import Role
from repositories.user_rep import AbstractUserRepository


class AbstractUserService(ABC):
    @abstractmethod
    async def get_user_by_id_or_raise(self, user_id: UUID) -> User:
        ...
    
    @abstractmethod       
    async def get_user_by_email_or_raise(self, email: str) -> User:
        ...
    
    @abstractmethod
    async def create_user(
        self,
        name: str,
        email: str,
        password: str,
        role: Role = Role.USER
    ) -> User:
        ...
    
    @abstractmethod
    async def get_users_list(self) -> List[User]:
        ...
    
    @abstractmethod
    async def update_user(self, user: User) -> User:
        ...
    
    @abstractmethod
    async def delete_user(self, user_id: UUID) -> None:
        ...
        

class UserService:
    def __init__(self, user_rep: AbstractUserRepository) -> None:
        self._user_rep = user_rep
        
    async def get_user_by_id_or_raise(self, user_id: UUID) -> User:
        user = await self._user_rep.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError(user_id=user_id)
        return user
    
    async def get_user_by_email_or_raise(self, email: str) -> User:
        user = await self._user_rep.get_by_email(email)
        if user is None:
            raise UserNotFoundError(email=email)
        return user
    
    async def create_user(
        self,
        name: str,
        email: str,
        password: str,
        role: Role = Role.USER
    ) -> User:
        return await self._user_rep.add(
            User(
                name=name,
                email=email,
                hashed_password=User.hash_password(password),
                role=role
            )
        )
    
    async def get_users_list(self) -> List[User]:
        return await self._user_rep.get_list()
    
    async def update_user(self, user: User) -> User:
        return await self._user_rep.update(user)
    
    async def delete_user(self, user_id: UUID) -> None:
        await self._user_rep.delete(user_id)
        