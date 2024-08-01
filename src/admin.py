from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from sqladmin import Admin, ModelView

from src.catalogue.models.database import (
    Category,
    Product,
    ProductCategory,
    ProductDiscount,
    ProductImage,
    StockRecord,
)

from src.basket.models.models import Basket
from src.users.models.database import User

from src.basket.admin import BasketAdmin


app = FastAPI()


DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)


admin = Admin(app, engine)

CATALOGUE_CATEGORY = 'Catalogue'
BASKET_CATEGORY = 'Basket'


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.title, Product.is_active]
    column_searchable_list = [Product.title, Product.description]
    form_columns = ['title', 'description', 'short_description', 'is_active']
    column_sortable_list = ['title', 'is_active']
    icon = 'fa-solid fa-box'
    category = CATALOGUE_CATEGORY

class BasketAdmin(ModelView, model=Basket):
    column_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    column_searchable_list = [Basket.id, Basket.user_id]
    form_columns = ['user_id', 'price', 'status']
    column_sortable_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    icon = 'fa-solid fa-shopping-basket'
    category = BASKET_CATEGORY

def register_admin_views(admin):
    admin.add_view(ProductAdmin)

    admin.add_view(BasketAdmin)

register_admin_views(admin)

@app.on_event("startup")
async def on_startup():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
