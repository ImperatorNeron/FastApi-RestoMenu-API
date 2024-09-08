from pydantic import BaseModel


class CategoryRead(BaseModel):
    id: int     # noqa
    name: str


class ListCategoryReadSchema(BaseModel):
    categories: list[CategoryRead]
