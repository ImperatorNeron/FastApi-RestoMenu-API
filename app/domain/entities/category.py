from dataclasses import dataclass
from typing import Optional


@dataclass
class CategoryEntity:
    title: str
    id: Optional[int] = None  # noqa
