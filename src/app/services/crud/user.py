from app.interfaces.uow import IUoW
from domain.entities.user import UserEntity


class UserCrudService:
    def __init__(self, uow: IUoW):
        self.uow = uow

    def register_user(self, user: UserEntity) -> None:
        with self.uow as uow:
            uow.rep.users.create(user)
            uow.commit()

        # set Cache

    def get(self, user_id: int) -> UserEntity | None:
        # try to get from Cache
        with self.uow as uow:
            return uow.rep.users.get(user_id)
