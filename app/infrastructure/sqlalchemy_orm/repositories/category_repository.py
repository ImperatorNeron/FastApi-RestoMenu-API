from sqlalchemy import (
    Result,
    select,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.common.repositories.abstract_category_repository import AbstractCategoryRepository
from app.infrastructure.sqlalchemy_orm.models.category import Category


class CategoryRepository(AbstractCategoryRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self) -> list[Category]:
        result: Result = await self.session.execute(select(Category))
        return list(result.scalars().all())

    async def add_category(self, category: Category) -> Category:
        self.session.add(category)
        await self.session.commit()
        return category
