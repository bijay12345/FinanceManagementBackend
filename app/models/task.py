from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
