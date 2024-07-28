from src.common.routes import BaseCrudPrefixes

class UserManagementRoutesPrefixes:
    user: str = '/user'

class UserRoutesPrefixes(BaseCrudPrefixes):
    def __init__(self):
        super().__init__()
        self.user_management = UserManagementRoutesPrefixes()

user_routes = UserRoutesPrefixes()
print(user_routes.create)
print(user_routes.user_management.user)
