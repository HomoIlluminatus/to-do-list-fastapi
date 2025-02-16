from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_session
from core.errors.user_error import UserNotFoundError
from entities.utils import Role
from schemas.user_dto import UserResponse
from services.user_service import AbstractUserService, UserService
from repositories.user_rep import AbstractUserRepository, UserRepository
from mappers.entities_dto import get_user_response


router = APIRouter(prefix='/users', tags=['Users'])


def get_user_repository(
    session: AsyncSession=Depends(get_async_session)
) -> AbstractUserRepository:
    return UserRepository(session)


def get_user_service(
    user_rep: AbstractUserRepository = Depends(get_user_repository)
) -> AbstractUserService:
    return UserService(user_rep)


@router.get('/by_email', response_model=UserResponse)
async def get_user_by_email(
    email: EmailStr,
    user_service: AbstractUserService=Depends(get_user_service)
) -> UserResponse:
    try:
        user = await user_service.get_user_by_email_or_raise(email)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    
    return get_user_response(user)


@router.get('/list', response_model=List[UserResponse])
async def get_users_list(
    user_service: AbstractUserService=Depends(get_user_service)
) -> List[UserResponse]:
    users = await user_service.get_users_list()
    return [get_user_response(user) for user in users]


@router.get('/{user_id}', response_model=UserResponse)
async def get_user_by_id(
    user_id: UUID, user_service: AbstractUserService=Depends(get_user_service)
) -> UserResponse:
    try:
        user = await user_service.get_user_by_id_or_raise(user_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    
    return get_user_response(user)


@router.post('/create_user', response_model=UserResponse)
async def create_user(
    name: str,
    email: str,
    password: str,
    role: Role=Role.USER,
    user_service: AbstractUserService=Depends(get_user_service)
) -> UserResponse:
    user = await user_service.create_user(name=name, email=email,
                                          password=password, role=role)
    return get_user_response(user)


@router.delete('/{user_id}', status_code=204)
async def delete_user(
    user_id: UUID, user_service: AbstractUserService=Depends(get_user_service)
) -> None:
    await user_service.delete_user(user_id)
    