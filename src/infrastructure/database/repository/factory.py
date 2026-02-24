from sqlalchemy.orm import Session

from app.interfaces.repository.factory import IRepositoryFactory
from infrastructure.database.repository.role import AlchemyRoleRepository
from infrastructure.database.repository.user import AlchemyUserRepository


class AlchemyRepositoryFactory(IRepositoryFactory):
    def __init__(self, session: Session):
        self._session = session

    @property
    def users(self) -> AlchemyUserRepository:
        return AlchemyUserRepository(self._session)

    @property
    def roles(self) -> AlchemyRoleRepository:
        return AlchemyRoleRepository(self._session)
