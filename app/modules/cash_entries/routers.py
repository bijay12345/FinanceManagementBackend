from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.database.base import get_db
from . import service
from .schemas import CashEntriesCreate, CashEntriesResponse, CashEntriesUpdate


router = APIRouter(prefix="/cashentries", tags=["cash entries"])


@router.post("/", response_model=CashEntriesResponse, status_code=201)
async def create_cash_entries(
    payload: CashEntriesCreate, db: AsyncSession = Depends(get_db)
):
    return await service.create_cash_entry(db, payload)


@router.get("/", response_model=CashEntriesResponse, status_code=200)
async def list_cash_entries(db: AsyncSession = Depends(get_db)):
    return service.list_cash_entries(db)
