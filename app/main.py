from fastapi import FastAPI
from app.modules.cash_entries.routers import router as cash_entries_routers
from app.modules.tasks.models import Task
from app.modules.cash_entries.models import CashEntries
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    DATABASE_URL = os.getenv("PROD_DB")

    app.state.engine = create_async_engine(
        DATABASE_URL, pool_size=10, max_overflow=20, echo=False
    )
    app.state.session_maker = async_sessionmaker(app.state.engine)

    print("🚀 Starting app...")
    yield
    await app.state.engine.dispose()
    print("🛑 Shutting down...")


app = FastAPI(
    title="Budget Management APIS",
    lifespan=lifespan,
)
app.include_router(cash_entries_routers)


@app.get("/")
def health_check():
    return {"health": "OK"}
