from fastapi import APIRouter, BackgroundTasks
from .category_service import CategoryService, CategoryIndex
from src.common.databases.redis import get_redis_client
from src.common.routes import BaseCrudPrefixes

router = APIRouter()

redis_client = get_redis_client()

class CatalogueRoutesPrefixes:
    product: str = '/product'

class ProductRoutesPrefixes(BaseCrudPrefixes):
    search: str = '/search'
    update_index: str = '/update-index'

@router.get(CatalogueRoutesPrefixes.product + ProductRoutesPrefixes.search)
async def search_categories(query: str):
    search = CategoryIndex.search().query("multi_match", query=query, fields=["title", "description"])
    response = search.execute()
    return response.to_dict()

@router.post(CatalogueRoutesPrefixes.product + ProductRoutesPrefixes.update_index)
async def update_index(background_tasks: BackgroundTasks):
    category_service = CategoryService(redis_client=redis_client)
    background_tasks.add_task(category_service.update_category_index)
    return {"message": "Index update started"}

@router.get("/index-status")
async def get_index_status():
    category_service = CategoryService(redis_client=redis_client)
    return {"status": category_service.get_index_status()}
