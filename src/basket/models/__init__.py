from sqlalchemy import Column, Integer, ForeignKey, Numeric, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class BasketStatus(enum.Enum):
    Open = "Open"
    Closed = "Closed"
    Cancelled = "Cancelled"

class Basket(Base):
    __tablename__ = 'baskets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    price = Column(Numeric)
    status = Column(Enum(BasketStatus))
