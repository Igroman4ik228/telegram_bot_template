from abc import ABC, abstractmethod

from domain.entities.user import UserEntity


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: UserEntity) -> None: ...

    @abstractmethod
    def get(self, user_id: int) -> UserEntity | None: ...
