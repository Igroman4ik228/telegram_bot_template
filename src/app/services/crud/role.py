from app.interfaces.uow import IUoW
from domain.entities.role import RoleEntity


class RoleCrudService:
    def __init__(self, uow: IUoW):
        self.uow = uow

    def register_role(self, role: RoleEntity) -> None:
        with self.uow as uow:
            uow.rep.roles.create(role)
            uow.commit()

        # set Cache

    def get(self, role_id: int) -> RoleEntity | None:
        # try to get from Cache
        with self.uow as uow:
            return uow.rep.roles.get(role_id)
