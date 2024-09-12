from typing import Annotated

from fastapi import Depends

from app.application.services.category_service import CategoryApplicationService
from app.infrastructure.common.repositories.abstract_category_repository import AbstractCategoryRepository
from app.infrastructure.repositories.category_repository import get_category_repository


def get_category_service(
    category_repository: Annotated[
        AbstractCategoryRepository, Depends(get_category_repository),
    ],
) -> CategoryApplicationService:
    return CategoryApplicationService(category_repository=category_repository)
