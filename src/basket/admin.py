from sqladmin import ModelView
from src.basket.models.basket import Basket
from src.common.databases.postgres import SessionLocal
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
from your_app import app

admin = Admin(app, session=SessionLocal, title="My Admin Interface")
register_admin_views(admin)
