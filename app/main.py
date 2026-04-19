from fastapi import FastAPI
from app.database.base import engine
from app.modules.cash_entries.routers import router as cash_entries_routers
from app.modules.tasks.models import Task
from app.modules.cash_entries.models import CashEntries
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting app...")
    yield
    print("🛑 Shutting down...")


app = FastAPI(
    title="Budget Management APIS",
    lifespan=lifespan,
)
app.include_router(cash_entries_routers)


@app.get("/")
def health_check():
    return {"health": "OK"}
