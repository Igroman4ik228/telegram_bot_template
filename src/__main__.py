import asyncio
from logging import INFO, NullHandler, basicConfig, getLogger

from app.services.user_service import UserService
from container import AppContainer
from persistence.db.db import DatabaseAlchemy
from persistence.db.models.user import UserOrm
from persistence.db.repositories.user import UserRepository

log = getLogger(__name__)
basicConfig(level=INFO)
getLogger("sqlalchemy.engine.Engine").handlers = [NullHandler()]


class App:
    def __init__(self, container: AppContainer):
        self.db = DatabaseAlchemy()

    async def start(self) -> None:
        await self.db.create_tables()

        async with self.db.get_session() as session:
            rep = UserRepository(session)
            await UserService(rep).register("user1")
            await session.commit()

            user = await rep.get(1)
            user2 = await rep.get(1)

            if user:
                user.name = "1"
                UserOrm(name="123")
                await rep.delete(user)
                await rep.save(user)
                await session.commit()

            user3 = await rep.get(1)

        if user:
            log.info(user.id)
            log.info(user.name)
            log.info(user.updated_at)
            log.info(user.created_at)

            log.info("\n")

        if user2:
            log.info(user2.id)
            log.info(user2.name)
            log.info(user2.updated_at)
            log.info(user2.created_at)
            log.info("\n")

        if user3:
            log.info(user3.id)

            log.info(user3.name)
            log.info(user3.updated_at)
            log.info(user3.created_at)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.db.close()


async def main() -> None:
    app_container = AppContainer()
    app_container.register_di()

    async with App(app_container) as app:
        await app.start()


if __name__ == "__main__":
    asyncio.run(main())
