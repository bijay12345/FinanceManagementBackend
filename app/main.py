from fastapi import FastAPI
from app.database.base import engine
from app.modules.cash_entries.routers import router as cash_entries_routers
from app.modules.tasks.models import Task
from app.modules.cash_entries.models import CashEntries


app = FastAPI(title="Budget Management APIS")
app.include_router(cash_entries_routers)


@app.get("/")
def health_check():
    return {"health": "OK"}
