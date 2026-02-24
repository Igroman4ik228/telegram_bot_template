from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from infrastructure.database.models.base import BaseOrm

if TYPE_CHECKING:
    from infrastructure.database.models.user import UserOrm


class RoleOrm(BaseOrm):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))

    users: Mapped[list["UserOrm"]] = relationship(
        back_populates="role",
    )
