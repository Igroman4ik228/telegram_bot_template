from domain.entities.user import UserEntity
from infrastructure.database.models.user import UserOrm
from infrastructure.mapper.pydantic import BasePydanticMapper


class UserMapper(BasePydanticMapper[UserEntity, UserOrm]):
    entity_cls = UserEntity
    orm_cls = UserOrm
