from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from src.catalogue.models.pydantic import CategoryCreate, CategoryUpdate, Category as CategoryModel
from src.catalogue.models.sqlalchemy import Category as CategorySQLModel
from src.common.databases.postgres import get_session
from src.common.repository.sqlalchemy import BaseSQLAlchemyRepository


class CategoryRepository(BaseSQLAlchemyRepository[CategorySQLModel, CategoryModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=CategorySQLModel, pydantic_model=CategoryModel, session=session)

    async def create(self, category: CategoryCreate) -> CategorySQLModel:
        db_category = self.model(**category.dict())
        self.session.add(db_category)
        await self.session.commit()
        await self.session.refresh(db_category)
        return db_category

    async def get(self, category_id: int) -> Optional[CategorySQLModel]:
        result = await self.session.execute(select(self.model).where(self.model.id == category_id).options(selectinload('*')))
        return result.scalars().first()

    async def list(self) -> List[CategorySQLModel]:
        result = await self.session.execute(select(self.model).options(selectinload('*')))
        return result.scalars().all()

    async def update(self, category_id: int, category: CategoryUpdate) -> Optional[CategorySQLModel]:
        db_category = await self.get(category_id)
        if db_category:
            for key, value in category.dict(exclude_unset=True).items():
                setattr(db_category, key, value)
            await self.session.commit()
            await self.session.refresh(db_category)
        return db_category

    async def delete(self, category_id: int) -> Optional[CategorySQLModel]:
        db_category = await self.get(category_id)
        if db_category:
            await self.session.delete(db_category)
            await self.session.commit()
        return db_category


def get_category_repository(session: AsyncSession = Depends(get_session)) -> CategoryRepository:
    return CategoryRepository(session=session)
