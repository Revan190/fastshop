import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqladmin import ModelView, Admin
from src.catalogue.models.database import (
    Category,
    Product,
    ProductCategory,
    ProductDiscount,
    ProductImage,
    StockRecord,
)
from basket.models import Basket, Base

print(Base)
print(Basket)

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db/fastapi_shop")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

CATALOGUE_CATEGORY = 'Catalogue'
SHOP_CATEGORY = 'Shop'

class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.title, Product.is_active]
    column_searchable_list = [Product.title, Product.description]
    form_columns = ['title', 'description', 'short_description', 'is_active']
    column_sortable_list = ['title', 'is_active']
    icon = 'fa-solid fa-box'
    category = CATALOGUE_CATEGORY

class ProductCategoryAdmin(ModelView, model=ProductCategory):
    column_list = [ProductCategory.product, ProductCategory.category]
    column_searchable_list = [ProductCategory.product_id, ProductCategory.category_id]
    form_columns = ['product', 'category']
    icon = 'fa-solid fa-tags'
    category = CATALOGUE_CATEGORY

class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.title, Category.is_active, Category.parent]
    column_searchable_list = [Category.title]
    form_columns = ['title', 'description', 'image', 'is_active', 'parent']
    icon = 'fa-solid fa-sitemap'
    category = CATALOGUE_CATEGORY

class ProductImageAdmin(ModelView, model=ProductImage):
    column_list = [ProductImage.product, ProductImage.original, ProductImage.thumbnail]
    column_searchable_list = [ProductImage.caption]
    form_columns = ['product', 'original', 'thumbnail', 'caption']
    icon = 'fa-solid fa-image'
    category = CATALOGUE_CATEGORY

class StockRecordAdmin(ModelView, model=StockRecord):
    column_list = [StockRecord.product, StockRecord.price, StockRecord.quantity]
    column_searchable_list = [StockRecord.price, StockRecord.quantity]
    form_columns = ['product', 'price', 'quantity', 'date_created', 'additional_info']
    icon = 'fa-solid fa-warehouse'
    category = CATALOGUE_CATEGORY

class ProductDiscountAdmin(ModelView, model=ProductDiscount):
    column_list = [ProductDiscount.product, ProductDiscount.discount_percent, ProductDiscount.discount_amount]
    column_searchable_list = [ProductDiscount.valid_from, ProductDiscount.valid_to]
    form_columns = ['product', 'discount_percent', 'discount_amount', 'valid_from', 'valid_to']
    icon = 'fa-solid fa-percent'
    category = CATALOGUE_CATEGORY

class BasketAdmin(ModelView, model=Basket):
    column_list = ['id', 'user_id', 'price', 'status']
    search_fields = ['id', 'user_id', 'status']
    icon = "fas fa-shopping-basket"
    category = SHOP_CATEGORY

def register_admin_views(admin):
    admin.add_view(ProductAdmin)
    admin.add_view(ProductCategoryAdmin)
    admin.add_view(CategoryAdmin)
    admin.add_view(ProductImageAdmin)
    admin.add_view(StockRecordAdmin)
    admin.add_view(ProductDiscountAdmin)
    admin.add_view(BasketAdmin)

admin = Admin(app, engine)
register_admin_views(admin)
