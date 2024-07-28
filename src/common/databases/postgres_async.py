from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from src.base_settings import base_settings

DATABASE_URL = base_settings.postgres.url

async_engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async_session = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
