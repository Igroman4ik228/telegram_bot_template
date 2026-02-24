from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.database.models.base import BaseOrm


class AlchemyDatabase:
    def __init__(self, url: str = "sqlite+pysqlite:///:memory:"):
        super().__init__()
        self._engine = create_engine(url, echo=True, future=True)
        self.session_maker = sessionmaker(
            bind=self._engine,
            expire_on_commit=False,
        )

    def create_tables(self) -> None:
        BaseOrm.metadata.create_all(self._engine)

    def close(self) -> None:
        self._engine.dispose()
