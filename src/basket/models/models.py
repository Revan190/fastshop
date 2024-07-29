from typing import List
from pydantic import BaseModel as PydanticBaseModel
from sqlalchemy import Column, Integer, ForeignKey, Numeric, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class BasketItem(PydanticBaseModel):
    product_id: int
    quantity: int

class PydanticBasket(PydanticBaseModel):
    id: int
    user_id: int
    items: List[BasketItem] = []

class BasketStatus(enum.Enum):
    Open = "Open"
    Closed = "Closed"   
    Cancelled = "Cancelled"

class SQLAlchemyBasket(Base):
    __tablename__ = 'baskets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    price = Column(Numeric)
    status = Column(Enum(BasketStatus))
