from fastapi import APIRouter

from app.api.schemas import ApiResponse
from app.api.v1.categories.schemas import (
    CategoryRead,
    ListCategoryReadSchema,
)


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.get("/", response_model=ApiResponse[ListCategoryReadSchema])
def get_categories():
    return ApiResponse(
        data=ListCategoryReadSchema(
            categories=[CategoryRead(id=1, name="First meal")],
        ),
    )
