from sqladmin import ModelView
from src.basket.models.models import Basket
from src.common.databases.postgres_async import get_session
from src.catalogue.admin import register_products_admin_views
from src.users.admin import register_users_admin_views

class BasketAdmin(ModelView, model=Basket):
    column_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    column_searchable_list = [Basket.user_id, Basket.status]
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
