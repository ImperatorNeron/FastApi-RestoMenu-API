from app.application.mappers.category_mapper import CategoryMapper
from app.domain.entities.category import CategoryEntity
from app.infrastructure.common.repositories.abstract_category_repository import AbstractCategoryRepository


# Need add Abstract class
class CategoryApplicationService:

    def __init__(self, category_repository: AbstractCategoryRepository):
        self.category_repository = category_repository

    async def get_all_categories(self):
        categories = await self.category_repository.get_all()
        return [CategoryMapper.to_entity(category) for category in categories]

    async def add_category(self, category_in: CategoryEntity):
        mapped_category_in = CategoryMapper.from_entity(category_in)
        category = await self.category_repository.add_category(mapped_category_in)
        return CategoryMapper.to_entity(category)
