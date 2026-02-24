from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from infrastructure.database.models.base import BaseOrm

if TYPE_CHECKING:
    from infrastructure.database.models.role import RoleOrm


class UserOrm(BaseOrm):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    fullname: Mapped[str | None] = mapped_column(String(100))

    role_id: Mapped[int | None] = mapped_column(
        ForeignKey("roles.id"),
    )

    role: Mapped["RoleOrm"] = relationship(
        back_populates="users",
        lazy="noload",
    )
