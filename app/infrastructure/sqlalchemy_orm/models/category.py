from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.infrastructure.sqlalchemy_orm.mixins.id_mixin import IdIntPkMixin
from app.infrastructure.sqlalchemy_orm.models.base import BaseModel


class Category(IdIntPkMixin, BaseModel):
    title: Mapped[str] = mapped_column(
        "Title",
        String(255),
        unique=True,
    )
