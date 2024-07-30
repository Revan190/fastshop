from pydantic import BaseModel, constr
from typing import Optional

class CategoryBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: bool = True
    parent_id: Optional[int] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    id: int

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
