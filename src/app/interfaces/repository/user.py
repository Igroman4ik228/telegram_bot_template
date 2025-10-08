from abc import ABC, abstractmethod

from domain.models.user import UserOrm


class IUserRepository(ABC):
    @abstractmethod
    def get(self, user_id: int) -> UserOrm | None: ...
