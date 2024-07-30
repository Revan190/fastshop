from fastapi import FastAPI
from sqladmin import Admin

from src.admin import register_admin_views
from src.base_settings import base_settings
from src.catalogue.views import product_router
from src.catalogue.routes import router as category_router
from src.common.databases.postgres import postgres
from src.general.views import router as status_router
from src.routes import BaseRoutesPrefixes

def include_routes(application: FastAPI) -> None:
    application.include_router(
        router=status_router,
    )
    application.include_router(
        router=product_router,
        prefix=BaseRoutesPrefixes.catalogue,
        tags=['Catalogue'],
    )
    application.include_router(
        router=category_router,
        prefix="/api",
        tags=['Categories'],
    )

def get_application() -> FastAPI:
    application = FastAPI(
        debug=base_settings.debug,
        docs_url=BaseRoutesPrefixes.swagger if base_settings.debug else None,
        redoc_url=BaseRoutesPrefixes.redoc if base_settings.debug else None,
        openapi_url=BaseRoutesPrefixes.openapi if base_settings.debug else None,
    )

    @application.on_event('startup')
    async def startup():
        postgres.connect(base_settings.postgres.url)
        engine = postgres.get_engine()
        admin = Admin(app=application, engine=engine)
        register_admin_views(admin)

        from src.common.databases.postgres import engine as async_engine
        from src.catalogue.models.sqlalchemy import SQLModel
        async with async_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    @application.on_event('shutdown')
    async def shutdown():
        await postgres.disconnect()

    include_routes(application)

    return application

app = get_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
