from sqlalchemy.ext.asyncio import AsyncSession

from persistence.db.models.user import UserOrm


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, model: UserOrm) -> None:
        self.session.add(model)
        await self.session.commit()

    async def get(self, user_id: int) -> UserOrm | None:
        return await self.session.get(UserOrm, user_id)
