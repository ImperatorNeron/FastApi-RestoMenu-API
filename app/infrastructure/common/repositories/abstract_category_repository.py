from abc import (
    ABC,
    abstractmethod,
)

from app.infrastructure.sqlalchemy_orm.models.category import Category


class AbstractCategoryRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[Category]: ...

    @abstractmethod
    async def add_category(self, category_in: Category) -> Category: ...
