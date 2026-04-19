from fastapi import FastAPI
from sqlalchemy import create_engine
from app.models.base import Base
from app.models.task import Task

user = "root"
password = ""
host = "127.0.0.1"
port = 3306
database = "budget_management_backend"

print(Base.metadata.tables)
app = FastAPI(title="Budget Management APIS")
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}", echo=True
)
Base.metadata.create_all(engine)


@app.get("/")
def health_check():
    return {"health": "OK"}
