from abc import ABC, abstractmethod

from domain.entities.role import RoleEntity


class IRoleRepository(ABC):
    @abstractmethod
    def create(self, role: RoleEntity) -> None: ...

    @abstractmethod
    def get(self, role_id: int) -> RoleEntity | None: ...
