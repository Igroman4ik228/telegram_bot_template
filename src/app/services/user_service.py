from logging import getLogger

from persistence.db.models.user import UserOrm
from persistence.db.repositories.user import UserRepository

log = getLogger(__name__)


class UserService:
    def __init__(self, rep: UserRepository):
        self.rep = rep

    async def register(self, name: str) -> UserOrm:
        user = UserOrm(name=name)
        log.info(f"До {user}")
        await self.rep.create(user)
        return user
