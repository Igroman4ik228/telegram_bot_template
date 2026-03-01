from logging import getLogger

from cashews import mem as cache
from sqlalchemy.ext.asyncio import AsyncSession

from persistence.db.models.user import UserOrm

log = getLogger(__name__)


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, model: UserOrm) -> None:
        await cache.delete(f"user:{model.id}")
        self.session.add(model)

    async def get(self, user_id: int) -> UserOrm | None:
        user_cached = await cache.get(f"user:{user_id}")
        if user_cached:
            return UserOrm.from_dict(user_cached)

        user = await self.session.get(UserOrm, user_id)
        if not user:
            return None

        await cache.set(
            f"user:{user_id}",
            user.to_dict(),
        )

        self.session.expunge(user)
        return user

    async def delete(self, model: UserOrm) -> None:
        await cache.delete(f"user:{model.id}")
        await self.session.delete(model)
