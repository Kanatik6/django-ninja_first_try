from ninja import Router
from typing import List
from .models import Product, Category
from .schemas import ProductSchema, ProductCreateSchema, CategorySchema, CategoryCreateSchema

router = Router()


# ===== КАТЕГОРИИ =====
@router.get("/categories", response=List[CategorySchema])
def list_categories(request):
    """Получить все категории"""
    return Category.objects.all()


@router.post("/categories", response=CategorySchema)
def create_category(request, data: CategoryCreateSchema):
    """Создать категорию"""
    category = Category.objects.create(**data.dict())
    return category


@router.get("/categories/{category_id}", response=CategorySchema)
def get_category(request, category_id: int):
    """Получить одну категорию"""
    return Category.objects.get(id=category_id)


@router.get("/categories/slug/{slug}", response=CategorySchema)
def get_category_by_slug(request, slug: str):
    """Получить категорию по slug"""
    return Category.objects.get(slug=slug)


# ===== ТОВАРЫ =====
@router.get("/products", response=List[ProductSchema])
def list_products(request, category_id: int = None, in_stock: bool = None):
    """Получить все товары с фильтрами"""
    products = Product.objects.select_related('category').all()

    if category_id:
        products = products.filter(category_id=category_id)

    if in_stock is not None:
        products = products.filter(in_stock=in_stock)

    return products


@router.post("/products", response=ProductSchema)
def create_product(request, data: ProductCreateSchema):
    """Создать товар"""
    product = Product.objects.create(**data.dict())
    return product


@router.get("/products/{product_id}", response=ProductSchema)
def get_product(request, product_id: int):
    """Получить один товар"""
    return Product.objects.select_related('category').get(id=product_id)


@router.get("/products/slug/{slug}", response=ProductSchema)
def get_product_by_slug(request, slug: str):
    """Получить товар по slug"""
    return Product.objects.select_related('category').get(slug=slug)


@router.delete("/products/{product_id}")
def delete_product(request, product_id: int):
    """Удалить товар"""
    product = Product.objects.get(id=product_id)
    product.delete()
    return {"success": True}
