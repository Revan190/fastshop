from typing import List, Optional
from fastapi import Depends

from src.catalogue.models.pydantic import CategoryCreate, CategoryUpdate, Category
from src.catalogue.repository import get_category_repository, CategoryRepository
from sqlalchemy.ext.asyncio import AsyncSession


class CategoryService:
    def __init__(self, repository: CategoryRepository):
        self.category_repository = repository

    async def create_category(self, category: CategoryCreate) -> Category:
        return await self.category_repository.create(category)

    async def get_category(self, category_id: int) -> Optional[Category]:
        return await self.category_repository.get(category_id)

    async def list_categories(self) -> List[Category]:
        return await self.category_repository.list()

    async def update_category(self, category_id: int, category: CategoryUpdate) -> Optional[Category]:
        return await self.category_repository.update(category_id, category)

    async def delete_category(self, category_id: int) -> Optional[Category]:
        return await self.category_repository.delete(category_id)


def get_category_service(repo: CategoryRepository = Depends(get_category_repository)) -> CategoryService:
    return CategoryService(repository=repo)
