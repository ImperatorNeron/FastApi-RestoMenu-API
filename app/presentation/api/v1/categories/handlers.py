from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)

from app.application.mappers.category_mapper import CategoryMapper
from app.application.services.category_service import CategoryApplicationService
from app.application.services.services import get_category_service
from app.presentation.api.schemas import ApiResponse
from app.presentation.api.v1.categories.schemas import (
    CategoryAddSchema,
    CategoryReadSchema,
    ListCategoryReadSchema,
)


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.get("/", response_model=ApiResponse[ListCategoryReadSchema])
async def get_categories(
    category_service: Annotated[CategoryApplicationService, Depends(get_category_service)],
):
    return ApiResponse(
        data=ListCategoryReadSchema(
            categories=[
                CategoryMapper.to_schema(category)
                for category in await category_service.get_all_categories()
            ],
        ),
    )


@router.post("/", response_model=ApiResponse[CategoryReadSchema])
async def add_category(
    category: CategoryAddSchema,
    category_service: Annotated[CategoryApplicationService, Depends(get_category_service)],
):
    category = await category_service.add_category(CategoryMapper.from_schema(category))
    return ApiResponse(
        data=CategoryMapper.to_schema(category),
    )
