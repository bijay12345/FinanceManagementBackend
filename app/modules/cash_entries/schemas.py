from pydantic import BaseModel, Field, field_validator
from typing import Optional
from decimal import Decimal
from datetime import date, datetime
from enum import Enum


class EntryType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class Mode(str, Enum):
    CASH = "cash"
    UPI = "upi"


class CashEntriesBase(BaseModel):
    entry_type: EntryType
    description: str = Field(..., max_length=300)
    amount: Decimal
    mode: Mode
    entry_date: date
    expense_head: str = Field(..., max_length=250)
    cash_enterable_type: Optional[str] = Field(default=None, max_length=250)
    cash_enterable_id: Optional[int] = None

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value: Decimal):
        if value <= 0:
            raise ValueError("Amount must be greater than 0")
        return value


class CashEntriesCreate(CashEntriesBase):
    pass


class CashEntriesUpdate(BaseModel):
    entry_type: Optional[EntryType] = None
    description: Optional[str] = None
    amount: Optional[Decimal] = None
    mode: Optional[Mode] = None
    entry_date: Optional[date] = None
    expense_head: Optional[str] = None
    cash_enterable_type: Optional[str] = None
    cash_enterable_id: Optional[int] = None


class CashEntriesResponse(CashEntriesBase):
    id: int
    created_at: datetime
    updated_at: datetime
