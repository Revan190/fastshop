from sqladmin import ModelView
from src.users.database import User, UserAddress
from src.common.databases.postgres import SessionLocal

ADMIN_CATEGORY = 'Accounts'

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.phone_number, User.is_admin, User.is_staff, User.is_active, User.first_name, User.last_name, User.date_joined, User.last_login, User.is_temporary]
    column_searchable_list = [User.email, User.phone_number, User.first_name, User.last_name]
    icon = 'fa-solid fa-user'
    category = ADMIN_CATEGORY

class UserAddressAdmin(ModelView, model=UserAddress):
    column_list = [UserAddress.user_id, UserAddress.title, UserAddress.city, UserAddress.street, UserAddress.house, UserAddress.apartment, UserAddress.post_code, UserAddress.floor, UserAddress.additional_info]
    column_searchable_list = [UserAddress.title, UserAddress.city, UserAddress.street, UserAddress.house, UserAddress.apartment]
    icon = 'fa-solid fa-address-book'
    category = ADMIN_CATEGORY

def register_users_admin_views(admin):
    admin.add_view(UserAdmin)
    admin.add_view(UserAddressAdmin)
