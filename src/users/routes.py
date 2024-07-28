from typing import Annotated, Union

from fastapi import APIRouter, Depends, status

from src.authentication.utils import get_current_user
from src.common.schemas.common import ErrorResponse
from src.users.models.user import User

class BaseCrudPrefixes:
    root: str = '/'
    create: str = '/create'
    read: str = '/read'
    update: str = '/update'
    delete: str = '/delete'

class UserManagementRoutesPrefixes:
    user: str = '/user'

class UserRoutesPrefixes(BaseCrudPrefixes):
    def __init__(self):
        super().__init__()
        self.user_management = UserManagementRoutesPrefixes()

user_routes = UserRoutesPrefixes()

router = APIRouter(prefix=user_routes.user_management.user)

@router.get(
    user_routes.root,
    responses={
        status.HTTP_200_OK: {'model': User},
        status.HTTP_404_NOT_FOUND: {'model': ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
    response_model=Union[User, ErrorResponse],
)
async def user_detail(
    current_user: Annotated[User, Depends(get_current_user)],
) -> Union[User, ErrorResponse]:
    """
    Retrieve user.

    Returns:
        Response with user details.
    """
    return current_user

print(user_routes.create)
print(user_routes.user_management.user)
