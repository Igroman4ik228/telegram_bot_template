from abc import ABC, abstractmethod
from typing import Self

from app.interfaces.repository.factory import IRepositoryFactory


class IUoW(ABC):
    @property
    @abstractmethod
    def rep(self) -> IRepositoryFactory: ...

    @abstractmethod
    def __enter__(self) -> Self: ...

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb): ...

    @abstractmethod
    def commit(self) -> None: ...
