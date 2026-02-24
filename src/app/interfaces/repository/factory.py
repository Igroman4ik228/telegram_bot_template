from abc import ABC, abstractmethod

from app.interfaces.repository.role import IRoleRepository
from app.interfaces.repository.user import IUserRepository


class IRepositoryFactory(ABC):
    @property
    @abstractmethod
    def users(self) -> IUserRepository: ...

    @property
    @abstractmethod
    def roles(self) -> IRoleRepository: ...
