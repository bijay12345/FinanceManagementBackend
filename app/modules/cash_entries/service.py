from .schemas import CashEntriesCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import CashEntries


async def create_cash_entry(db: AsyncSession, data: CashEntriesCreate):
    obj = CashEntries(**data.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def list_cash_entries(db: AsyncSession, skip: int = 0, limit: int = 0):
    data = await db.execute(
        select(CashEntries)
        .offset(skip)
        .limit(limit)
        .order_by(CashEntries.created_at.desc())
    )
    return data.scalars().all()
