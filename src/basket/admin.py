from sqladmin import ModelView
from src.basket.models.models import SQLAlchemyBasket
from src.common.databases.postgres_async import get_session
from src.catalogue.admin import register_products_admin_views
from src.users.admin import register_users_admin_views

class BasketAdmin(ModelView, model=SQLAlchemyBasket):
    column_list = [SQLAlchemyBasket.id, SQLAlchemyBasket.user_id, SQLAlchemyBasket.price, SQLAlchemyBasket.status]
    column_searchable_list = [SQLAlchemyBasket.user_id, SQLAlchemyBasket.status]
    icon = "fa-shopping-basket"
    category = "E-commerce"

def register_admin_views(admin):
    register_users_admin_views(admin=admin)
    register_products_admin_views(admin=admin)
    admin.add_view(BasketAdmin)

from sqladmin import Admin
from fastapi import FastAPI

app = FastAPI()

admin = Admin(app, session=get_session, title="My Admin Interface")
register_admin_views(admin)
