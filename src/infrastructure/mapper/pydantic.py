from domain.entities.pydantic import PydanticEntity
from infrastructure.database.models.base import BaseOrm


class BasePydanticMapper[TEntity: PydanticEntity, TOrm: BaseOrm]:
    entity_cls: type[TEntity]
    orm_cls: type[TOrm]

    @classmethod
    def orm(cls, entity: TEntity) -> TOrm:
        return cls.orm_cls(**entity.model_dump())

    @classmethod
    def entity(cls, orm: TOrm) -> TEntity:
        return cls.entity_cls.model_validate(orm)
