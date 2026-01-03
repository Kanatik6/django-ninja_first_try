from ninja import Schema
from datetime import datetime


class CategorySchema(Schema):
    id: int
    name: str
    description: str
    icon: str
    is_active: bool
    order: int
    created_at: datetime
    updated_at: datetime


class CategoryCreateSchema(Schema):
    name: str
    description: str = ""
    icon: str = ""
    is_active: bool = True
    order: int = 0


class ProductSchema(Schema):
    id: int
    name: str
    description: str
    price: float
    category: CategorySchema
    in_stock: bool
    created_at: datetime


class ProductCreateSchema(Schema):
    name: str
    description: str
    price: float
    category_id: int
    in_stock: bool = True
