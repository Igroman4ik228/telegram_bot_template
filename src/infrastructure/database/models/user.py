from sqlalchemy import Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from infrastructure.database.models.base import BaseOrm


class UserOrm(BaseOrm):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    fullname: Mapped[str | None] = mapped_column(String(100))
