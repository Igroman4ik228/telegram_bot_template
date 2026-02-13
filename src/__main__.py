import asyncio
from logging import INFO, basicConfig, getLogger

from app.services.user_service import UserService
from container import AppContainer
from persistence.db.db import DatabaseAlchemy
from persistence.db.repositories.user import UserRepository

log = getLogger(__name__)
basicConfig(level=INFO)


class App:
    def __init__(self, container: AppContainer):
        self.db = DatabaseAlchemy()

    async def start(self) -> None:
        await self.db.create_tables()

        async with self.db.get_session() as session:
            rep = UserRepository(session)
            user = await UserService(rep).register("user1")

        log.info(user)

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
