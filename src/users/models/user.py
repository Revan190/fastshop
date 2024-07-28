from datetime import datetime
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    phone_number: str
    hashed_password: Optional[str]
    is_admin: bool = False
    is_staff: bool = False
    is_active: bool = True
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_joined: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = None
    is_temporary: bool = False

    addresses: List["UserAddress"] = Relationship(back_populates="user")
