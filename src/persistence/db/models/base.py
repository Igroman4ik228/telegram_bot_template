from datetime import datetime
from typing import Annotated

from sqlalchemy import BigInteger, DateTime, SmallInteger, String, func
from sqlalchemy.orm import (
    DeclarativeBase,
    MappedAsDataclass,
    mapped_column,
    registry,
)

CreatedAt = Annotated[
    datetime,
    mapped_column(server_default=func.now()),
]
UpdatedAt = Annotated[
    datetime,
    mapped_column(
        server_default=func.now(),
        server_onupdate=func.now(),
    ),
]

type Int16 = Annotated[int, 16]
type Int64 = Annotated[int, 64]

type Str128 = Annotated[str, 128]
type Str512 = Annotated[str, 512]
type Str1024 = Annotated[str, 1024]
type Str2048 = Annotated[str, 2048]
type Str8192 = Annotated[str, 8192]


class BaseAlchemyOrm(MappedAsDataclass, DeclarativeBase):
    registry = registry(
        type_annotation_map={
            Int16: SmallInteger(),
            Int64: BigInteger(),
            Str128: String(128),
            Str512: String(512),
            Str1024: String(1024),
            Str2048: String(2048),
            Str8192: String(8192),
            datetime: DateTime(timezone=True),
        },
    )
