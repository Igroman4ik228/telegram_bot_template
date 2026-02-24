from domain.entities.pydantic import PydanticEntity


class RoleEntity(PydanticEntity):
    name: str
    description: str | None = None

    def greet(self) -> str:
        return f"Role: {self.name}"
