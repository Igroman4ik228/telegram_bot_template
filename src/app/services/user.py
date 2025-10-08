from app.interfaces.uow import IUoW
from domain.models.user import UserOrm


class UserCrudService:
    def __init__(self, uow: IUoW):
        self.uow = uow

    def register_user(self, user: UserOrm) -> None:
        with self.uow as uow:
            uow.commit(user)

        # set Cache

    def get(self, user_id: int) -> UserOrm | None:
        # try to get from Cache
        with self.uow as uow:
            return uow.rep.users.get(user_id)
