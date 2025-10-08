from sqlalchemy.orm import Session

from app.interfaces.repository.user import IUserRepository
from domain.models.user import UserOrm


class AlchemyUserRepository(IUserRepository):
    def __init__(self, session: Session):
        self._session = session

    def get(self, user_id: int) -> UserOrm | None:
        user = self._session.query(UserOrm).filter_by(id=user_id).first()
        if not user:
            return None

        return user
