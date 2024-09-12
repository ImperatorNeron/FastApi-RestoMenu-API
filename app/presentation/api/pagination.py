from typing import (
    Generic,
    TypeVar,
)

from pydantic import BaseModel


TListItem = TypeVar("TListItem")


class PaginationIn(BaseModel):
    offset: int = 0
    limit: int = 20


class PaginationOut(BaseModel):
    offset: int
    limit: int
    total: int


class LispPaginatedResponse(BaseModel, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOut
