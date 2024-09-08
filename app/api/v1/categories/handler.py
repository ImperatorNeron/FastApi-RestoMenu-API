from fastapi import APIRouter

from api.schemas import ApiResponse
from api.v1.categories.schemas import (
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
