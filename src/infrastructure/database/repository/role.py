from sqlalchemy.orm import Session

from app.interfaces.repository.role import IRoleRepository
from domain.entities.role import RoleEntity
from infrastructure.database.models.role import RoleOrm
from infrastructure.mapper.role import RoleMapper


class AlchemyRoleRepository(IRoleRepository):
    def __init__(self, session: Session):
        self._session = session

    def create(self, role: RoleEntity) -> None:
        self._session.add(RoleMapper.orm(role))

    def get(self, role_id: int) -> RoleEntity | None:
        role = self._session.query(RoleOrm).filter_by(id=role_id).first()
        if role:
            return RoleMapper.entity(role)
        return None
