from rodi import Container

from app.interfaces.uow import IUoW
from app.services.user import UserCrudService
from infrastructure.database.db import AlchemyDatabase
from infrastructure.database.uow import AlchemyUoW


class AppContainer(Container):
    def __init__(self):
        super().__init__()

    def register_di(self) -> None:
        self.add_singleton_by_factory(
            lambda: AlchemyDatabase(),
            AlchemyDatabase,
        )
        self.add_scoped_by_factory(
            lambda c: AlchemyUoW(c.get(AlchemyDatabase).session_maker),
            IUoW,
        )
        self.add_scoped(
            UserCrudService,
        )
