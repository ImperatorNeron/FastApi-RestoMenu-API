from app.domain.entities.category import CategoryEntity
from app.infrastructure.sqlalchemy_orm.models.category import Category
from app.presentation.api.v1.categories.schemas import (
    CategoryAddSchema,
    CategoryReadSchema,
)


class CategoryMapper:

    @staticmethod
    def to_entity(orm_model: Category):
        return CategoryEntity(id=orm_model.id, title=orm_model.title)

    @staticmethod
    def from_entity(entity: CategoryEntity):
        return Category(id=entity.id, title=entity.title)

    @staticmethod
    def from_schema(schema: CategoryAddSchema):
        return CategoryEntity(title=schema.title)

    @staticmethod
    def to_schema(entity: CategoryEntity):
        return CategoryReadSchema(id=entity.id, title=entity.title)
