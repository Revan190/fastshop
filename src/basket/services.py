from src.basket.models.models import PydanticBasket, BasketItem, SQLAlchemyBasket
from sqlalchemy.orm import Session

def add_item_to_basket(basket: PydanticBasket, item: BasketItem):
    basket.items.append(item)

def remove_item_from_basket(basket: PydanticBasket, product_id: int):
    basket.items = [item for item in basket.items if item.product_id != product_id]

def get_total_items(basket: PydanticBasket):
    return sum(item.quantity for item in basket.items)

def create_basket_in_db(db: Session, basket: SQLAlchemyBasket):
    db.add(basket)
    db.commit()
    db.refresh(basket)
    return basket
