from ...models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Numeric, DateTime
from decimal import Decimal
from datetime import date, datetime
from typing import Optional


class CashEntries(Base):
    __tablename__ = "cash_entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    entry_type: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(300))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    mode: Mapped[str] = mapped_column(String(50))
    entry_date: Mapped[date] = mapped_column(Date())
    expense_head: Mapped[str] = mapped_column(String(250))
    cash_enterable_type: Mapped[Optional[str]] = mapped_column(
        String(250), nullable=True
    )
    cash_enterable_id: Mapped[Optional[int]] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )
