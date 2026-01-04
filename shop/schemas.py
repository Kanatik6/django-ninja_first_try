from ninja import Schema
from datetime import datetime
from typing import List


class CategorySchema(Schema):
    id: int
    name: str
    slug: str
    description: str
    icon: str
    is_active: bool
    order: int
    created_at: datetime
    updated_at: datetime


class CategoryCreateSchema(Schema):
    name: str
    slug: str = ""
    description: str = ""
    icon: str = ""
    is_active: bool = True
    order: int = 0


class ProductSchema(Schema):
    id: int
    name: str
    slug: str
    description: str
    price: float
    category: CategorySchema
    images: List[str] = []
    in_stock: bool
    created_at: datetime


class ProductCreateSchema(Schema):
    name: str
    slug: str = ""
    description: str
    price: float
    category_id: int
    images: List[str] = []
    in_stock: bool = True