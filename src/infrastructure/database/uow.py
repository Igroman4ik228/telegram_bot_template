from typing import Self

from sqlalchemy.orm import Session, sessionmaker

from app.interfaces.uow import IUoW
from domain.models.base import BaseOrm
from infrastructure.database.repository.factory import AlchemyRepositoryFactory


class AlchemyUoW(IUoW):
    def __init__(
        self,
        session_maker: sessionmaker[Session],
        *,
        commit: bool = False,
    ):
        self._session_maker = session_maker
        self._commit = commit
        self._session: Session | None = None
        self._repository_factory: AlchemyRepositoryFactory | None = None

    @property
    def rep(self) -> AlchemyRepositoryFactory:
        if self._repository_factory is None:
            msg = "UoW is not initialized. Use `with` context."
            raise RuntimeError(msg)

        return self._repository_factory

    def __enter__(self) -> Self:
        self._session = self._session_maker().__enter__()
        self._repository_factory = AlchemyRepositoryFactory(self._session)
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        if self._session is None:
            return
        try:
            if self._commit and exc_type is None:
                self._session.commit()
        except Exception:
            self._session.rollback()
        finally:
            self._session.close()
            self._session = None
            self._repository_factory = None

    def commit(self, *instances: BaseOrm) -> None:
        if self._session is None:
            msg = "Session is not initialized."
            raise RuntimeError(msg)

        for instance in instances:
            self._session.merge(instance)

        self._session.commit()

    def merge(self, *instances: BaseOrm) -> None: ...

    def delete(self, *instances: BaseOrm) -> None: ...
