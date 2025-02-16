from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_session
from core.errors.category_error import CategoryNotFoundError
from repositories.category_rep import (
    AbstractCategoryRepository,
    CategoryRepository,
) 
from services.category_service import AbstractCategoryService, CategoryService
from schemas.category_dto import CategoryResponse
from mappers.entities_dto import get_category_response


router = APIRouter(prefix='/categories', tags=['Categories'])


def get_category_repository(
    session: AsyncSession=Depends(get_async_session)    
) -> AbstractCategoryRepository:
    return CategoryRepository(session)


def get_category_service(
    category_rep: AbstractCategoryRepository=Depends(get_category_repository)
) -> AbstractCategoryService:
    return CategoryService(category_rep)


@router.get('/list', response_model=List[CategoryResponse])
async def get_categories_list(
    category_service: AbstractCategoryService=Depends(get_category_service)
) -> CategoryResponse:
    categories = await category_service.get_categories_list()
    return [get_category_response(category) for category in categories]


@router.get('/list/{user_id}', response_model=List[CategoryResponse])
async def get_user_categories_list(
    user_id: UUID,
    category_service: AbstractCategoryService=Depends(get_category_service) 
) -> List[CategoryResponse]:
    categories = await category_service.get_user_categories_list(user_id)
    return [get_category_response(category) for category in categories]


@router.get('/{category_id}', response_model=CategoryResponse)
async def get_category(
    category_id: UUID,
    category_service: AbstractCategoryService=Depends(get_category_service)
) -> CategoryResponse:
    try:
        category = await category_service.get_category_or_raise(category_id)
    except CategoryNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    return get_category_response(category)


@router.post('/create_category', response_model=CategoryResponse)
async def create_category(
    user_id: UUID,
    title: str,
    description: Optional[str] = None,
    category_service: AbstractCategoryService=Depends(get_category_service)
) -> CategoryResponse:
    return await category_service.create_category(user_id=user_id, title=title,
                                                  description=description)
    

@router.delete('/{category_id}', status_code=204)
async def delete_categpry(
    category_id: UUID,
    category_service: AbstractCategoryService=Depends(get_category_service)
) -> None:
    await category_service.delete_category(category_id)
    