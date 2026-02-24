from domain.entities.role import RoleEntity
from infrastructure.database.models.role import RoleOrm
from infrastructure.mapper.pydantic import BasePydanticMapper


class RoleMapper(BasePydanticMapper[RoleEntity, RoleOrm]):
    entity_cls = RoleEntity
    orm_cls = RoleOrm
