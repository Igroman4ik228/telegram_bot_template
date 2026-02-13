from sqlalchemy.orm import Mapped

from persistence.db.models.base import BaseAlchemyOrm
from persistence.db.models.mixins.int_id import IntPkMixin
from persistence.db.models.mixins.timestamp import TimestampMixin


class UserOrm(BaseAlchemyOrm, IntPkMixin, TimestampMixin):
    __tablename__ = "user"

    name: Mapped[str]
