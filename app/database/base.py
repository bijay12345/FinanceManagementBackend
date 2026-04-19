from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import create_engine
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.models.base import Base


user = "root"
password = ""
host = "127.0.0.1"
port = 3306
database = "budget_management_backend"
DATABASE_URL = f"mysql+aiomysql://{user}:{password}@{host}:{port}/{database}"

engine = create_async_engine(DATABASE_URL)


AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
