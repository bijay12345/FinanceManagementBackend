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


@router.get("/", response_model=list[CashEntriesResponse])
async def list_cash_entries(db: AsyncSession = Depends(get_db)):
    data = await service.list_cash_entries(db)
    return data


@router.get("/{id}", response_model=CashEntriesResponse)
async def get_cash_entry(id: int, db: AsyncSession = Depends(get_db)):
    entry = await service.get_cash_entry(id, db)
    return entry


@router.put("/{id}", response_model=CashEntriesResponse)
async def update_cash_entry(
    id: int, data: CashEntriesUpdate, db: AsyncSession = Depends(get_db)
):
    updated_data = await service.update_cash_entry(id, data, db)
    return updated_data


@router.delete("/{id}")
async def delete_cash_entry(id: int, db: AsyncSession = Depends(get_db)):
    await service.delete_cash_entry(id, db)
    return {"status": "deleted"}
