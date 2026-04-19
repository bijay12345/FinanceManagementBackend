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


async def list_cash_entries(db: AsyncSession, skip: int = 0, limit: int = 10):
    data = await db.execute(
        select(CashEntries)
        .limit(limit)
        .offset(skip)
        .order_by(CashEntries.created_at.desc())
    )
    return data.scalars().all()
