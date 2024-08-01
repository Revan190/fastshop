from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from .user import User

class UserAddress(SQLModel, table=True):
    __tablename__ = 'user_addresses'

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    title: Optional[str] = None
    city: str
    street: str
    house: str
    apartment: Optional[str] = None
    post_code: Optional[str] = None
    floor: Optional[str] = None
    additional_info: Optional[str] = None

    user: User = Relationship(back_populates="addresses")
