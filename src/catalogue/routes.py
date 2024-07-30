from fastapi import APIRouter, Depends, HTTPException
from typing import List

from src.catalogue.models.pydantic import CategoryCreate, Category, CategoryUpdate
from src.catalogue.services import get_category_service, CategoryService

router = APIRouter()

@router.post("/categories/", response_model=Category)
async def create_category(category: CategoryCreate, service: CategoryService = Depends(get_category_service)):
    return await service.create_category(category)

@router.get("/categories/", response_model=List[Category])
async def list_categories(service: CategoryService = Depends(get_category_service)):
    return await service.list_categories()

@router.get("/categories/{category_id}", response_model=Category)
async def get_category(category_id: int, service: CategoryService = Depends(get_category_service)):
    category = await service.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/categories/{category_id}", response_model=Category)
async def update_category(category_id: int, category: CategoryUpdate, service: CategoryService = Depends(get_category_service)):
    updated_category = await service.update_category(category_id, category)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

@router.delete("/categories/{category_id}", response_model=Category)
async def delete_category(category_id: int, service: CategoryService = Depends(get_category_service)):
    deleted_category = await service.delete_category(category_id)
    if not deleted_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category
