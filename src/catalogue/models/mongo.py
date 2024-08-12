from beanie import Document
from beanie.odm.fields import PydanticObjectId

class ProductAnalytics(Document):
    product_id: int
    timestamp: datetime

    class Settings:
        collection = "product_analytics"
        