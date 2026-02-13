from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from persistence.db.models.base import BaseAlchemyOrm


class DatabaseAlchemy:
    def __init__(
        self,
        url: str = "sqlite+aiosqlite:///:memory:",
        echo: bool = False,
    ):
        self._engine = create_async_engine(
            url=url,
            echo=echo,
        )

        self._sessionmaker = async_sessionmaker(
            bind=self._engine,
            autoflush=False,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._sessionmaker() as session:
            yield session

    async def create_tables(self) -> None:
        async with self._engine.begin() as conn:
            await conn.run_sync(BaseAlchemyOrm.metadata.create_all)

    async def get_session_maker(self) -> async_sessionmaker[AsyncSession]:
        return self._sessionmaker

    async def close(self) -> None:
        await self._engine.dispose()
