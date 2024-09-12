from typing import Annotated

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.common.repositories.abstract_category_repository import AbstractCategoryRepository
from app.infrastructure.sqlalchemy_orm.database import database_helper
from app.infrastructure.sqlalchemy_orm.repositories.category_repository import CategoryRepository


def get_category_repository(
    session: Annotated[AsyncSession, Depends(database_helper.session_getter)],
) -> AbstractCategoryRepository:
    return CategoryRepository(session=session)
