from .schemas import CashEntriesCreate, CashEntriesUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import CashEntries
from fastapi import Response


async def create_cash_entry(db: AsyncSession, data: CashEntriesCreate):
    obj = CashEntries(**data.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def list_cash_entries(db: AsyncSession, skip: int = 0, limit: int = 10):
    data = await db.execute(
        select(CashEntries)
        .limit(limit)
        .offset(skip)
        .order_by(CashEntries.created_at.desc())
    )
    return data.scalars().all()


async def get_cash_entry(id: int, db: AsyncSession):
    data = await db.execute(select(CashEntries).where(CashEntries.id == id))
    return data.scalar_one_or_none()


async def update_cash_entry(id: int, data: CashEntriesUpdate, db: AsyncSession):
    record = await db.get(CashEntries, id)
    if not record:
        return Response("Item not found")

    update_record = data.model_dump(exclude_unset=True)
    for key, value in update_record.items():
        setattr(record, key, value)
    await db.commit()
    await db.refresh(record)
    return record


async def delete_cash_entry(id: int, db: AsyncSession):
    record = await db.get(CashEntries, id)
    if not record:
        return Response("Item not found")
    await db.delete(record)
    await db.commit()
    return id
