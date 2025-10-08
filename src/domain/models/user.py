from sqlalchemy import Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from domain.models.base import BaseOrm


class UserOrm(BaseOrm):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str | None] = mapped_column(String(100))

    @property
    def full_name(self) -> str:
        if self.last_name is None:
            return self.first_name
        return f"{self.first_name} {self.last_name}"
