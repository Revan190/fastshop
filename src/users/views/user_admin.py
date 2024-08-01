from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from src.authentication.utils import get_current_admin
from src.common.databases import get_session
from src.common.schemas.common import ErrorResponse
from src.users.models.user import User
from src.users.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

@router.post(
    "/users/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse}},
)
async def create_user(
    *,
    session: Session = Depends(get_session),
    user: UserCreate,
    current_admin: User = Depends(get_current_admin),
) -> UserRead:
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@router.get(
    "/users/",
    response_model=List[UserRead],
    status_code=status.HTTP_200_OK,
)
async def read_users(
    *,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin),
) -> List[UserRead]:
    users = session.exec(select(User)).all()
    return users

@router.get(
    "/users/{user_id}",
    response_model=UserRead,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorResponse}},
)
async def read_user(
    *,
    user_id: int,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin),
) -> Union[UserRead, ErrorResponse]:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.put(
    "/users/{user_id}",
    response_model=UserRead,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorResponse}},
)
async def update_user(
    *,
    user_id: int,
    user_update: UserUpdate,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin),
) -> Union[UserRead, ErrorResponse]:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user_data = user_update.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorResponse}},
)
async def delete_user(
    *,
    user_id: int,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin),
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    session.delete(user)
    session.commit()
