from sqlalchemy.orm import Session

from app.interfaces.repository.user import IUserRepository
from domain.entities.user import UserEntity
from infrastructure.database.models.user import UserOrm
from infrastructure.mapper.user import UserMapper


class AlchemyUserRepository(IUserRepository):
    def __init__(self, session: Session):
        self._session = session

    def create(self, user: UserEntity) -> None:
        self._session.add(UserMapper.orm(user))

    def get(self, user_id: int) -> UserEntity | None:
        user = self._session.query(UserOrm).filter_by(id=user_id).first()
        if user:
            return UserMapper.entity(user)
        return None
