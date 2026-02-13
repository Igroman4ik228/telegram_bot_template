from sqlalchemy.orm import Mapped

from persistence.db.models.base import CreatedAt, UpdatedAt, mapped_column


class TimestampMixin:
    created_at: Mapped[CreatedAt] = mapped_column(init=False)
    updated_at: Mapped[UpdatedAt] = mapped_column(init=False)
