from datetime import datetime
from beanie import Document
from beanie.odm.fields import IntField, DateTimeField

class ProductAnalytics(Document):
    product_id: int
    timestamp: datetime

    class Settings:
        collection = "product_analytics"
