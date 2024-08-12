from beanie import init_beanie, PydanticObjectId
from beanie.odm.operators.update.general import Set
from ..common.databases.mongo_db import get_database
from .models.mongo import ProductAnalytics

class ProductAnalyticsRepository:
    def __init__(self):
        self.collection = ProductAnalytics

    async def insert_one(self, product_analytics: ProductAnalytics):
        await product_analytics.insert()

    async def get_all(self):
        return await self.collection.find_all().to_list()

    async def get_by_id(self, product_id: int):
        return await self.collection.find_one(self.collection.product_id == product_id)

async def init_product_analytics_repository():
    db = await get_database()
    await init_beanie(database=db, document_models=[ProductAnalytics])
    return ProductAnalyticsRepository()
    