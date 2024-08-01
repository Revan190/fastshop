from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from src.authentication.utils import get_current_admin
from src.common.databases import get_session
from src.common.schemas.common import ErrorResponse
from src.users.models.user_address import UserAddress
from src.users.schemas.user_address import UserAddressCreate, UserAddressRead, UserAddressUpdate

router = APIRouter()

@router.post(
    "/addresses/",
    response_model=UserAddressRead,
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse}},
)
async def create_address(
    *,
    session: Session = Depends(get_session),
    address: UserAddressCreate,
    current_admin: User = Depends(get_current_admin),
) -> UserAddressRead:
    db_address = UserAddress.from_orm(address)
    session.add(db_address)
    session.commit()
    session.refresh(db_address)
    return db_address

@router.get(
    "/addresses/",
    response_model=List[UserAddressRead],
    status_code=status.HTTP_200_OK,
)
async def read_addresses(
    *,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin),
) -> List[UserAddressRead]:
    addresses = session.exec(select(UserAddress)).all()
    return addresses

@router.get(
    "/addresses/{address_id}",
    response_model=UserAddressRead,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorResponse}},
)
async def read_address(
    *,
    address_id: int,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin),
) -> Union[UserAddressRead, ErrorResponse]:
    address = session.get(UserAddress, address_id)
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")
    return address

@router.put(
    "/addresses/{address_id}",
    response_model=UserAddressRead,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorResponse}},
)
async def update_address(
    *,
    address_id: int,
    address_update: UserAddressUpdate,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin),
) -> Union[UserAddressRead, ErrorResponse]:
    address = session.get(UserAddress, address_id)
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")
    address_data = address_update.dict(exclude_unset=True)
    for key, value in address_data.items():
        setattr(address, key, value)
    session.add(address)
    session.commit()
    session.refresh(address)
    return address

@router.delete(
    "/addresses/{address_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorResponse}},
)
async def delete_address(
    *,
    address_id: int,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin),
):
    address = session.get(UserAddress, address_id)
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")
    session.delete(address)
    session.commit()
