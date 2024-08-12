from fastapi import APIRouter, Depends
from .services import ProductService, ProductAnalyticsService
from .repository import init_product_repository, init_product_analytics_repository
from .models.pydantic import ProductModel

router = APIRouter()

async def get_product_service() -> ProductService:
    repository = await init_product_repository()
    return ProductService(repository=repository)

async def get_product_analytics_service() -> ProductAnalyticsService:
    repository = await init_product_analytics_repository()
    return ProductAnalyticsService(product_analytics_repo=repository)

@router.get("/product_detail/{product_id}")
async def product_detail(product_id: int, 
                         product_service: ProductService = Depends(get_product_service),
                         analytics_service: ProductAnalyticsService = Depends(get_product_analytics_service)):

    await analytics_service.record_product_visit(product_id)

    return {"message": f"Product {product_id} visited and analytics recorded"}