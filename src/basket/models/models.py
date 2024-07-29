from sqlalchemy import Column, Integer, ForeignKey, Enum, Numeric
from sqlalchemy.orm import relationship
from src.users.models.database import User
from src.common.databases import Base
import enum

class BasketStatus(enum.Enum):
    OPEN = "Open"
    CLOSED = "Closed"
    CANCELLED = "Cancelled"

class Basket(Base):
    __tablename__ = 'baskets'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    price = Column(Numeric(10, 2))
    status = Column(Enum(BasketStatus), default=BasketStatus.OPEN)

    user = relationship("User")
