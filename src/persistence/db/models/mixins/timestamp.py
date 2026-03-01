from sqlalchemy.orm import Mapped

from persistence.db.models.base import CreatedAt, UpdatedAt


class TimestampMixin:
    __mapper_args__ = {"eager_defaults": True}

    created_at: Mapped[CreatedAt]
    updated_at: Mapped[UpdatedAt]
