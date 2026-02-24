from domain.entities.pydantic import PydanticEntity


class UserEntity(PydanticEntity):
    username: str
    fullname: str | None = None
    role_id: int | None = None

    def greet(self) -> str:
        return f"Hi, {self.fullname}"
