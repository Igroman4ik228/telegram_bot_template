from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict


class PydanticEntity(PydanticBaseModel):
    model_config = ConfigDict(
        extra="ignore",
        from_attributes=True,
        populate_by_name=True,
    )
