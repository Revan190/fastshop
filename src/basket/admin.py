from sqladmin import ModelView
from src.basket.models.models import Basket, BasketStatus
from src.users.models.database import User

BASKET_CATEGORY = 'Basket'

class BasketAdmin(ModelView, model=Basket):
    column_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    column_searchable_list = [Basket.id, Basket.user_id]
    form_columns = ['user_id', 'price', 'status']
    column_sortable_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    icon = 'fa-solid fa-shopping-basket'
    category = BASKET_CATEGORY
