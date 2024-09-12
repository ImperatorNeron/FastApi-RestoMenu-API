from pydantic import BaseModel


class CategoryReadSchema(BaseModel):
    id: int     # noqa
    title: str


class CategoryAddSchema(BaseModel):
    title: str


class ListCategoryReadSchema(BaseModel):
    categories: list[CategoryReadSchema]
