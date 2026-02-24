from app.services.crud.role import RoleCrudService
from app.services.crud.user import UserCrudService
from container import AppContainer
from domain.entities.role import RoleEntity
from domain.entities.user import UserEntity
from infrastructure.database.db import AlchemyDatabase


class App:
    def __init__(self, container: AppContainer):
        self.db = container.resolve(AlchemyDatabase)
        self.user_service = container.resolve(UserCrudService)
        self.role_service = container.resolve(RoleCrudService)

    def start(self) -> None:
        # Delete this after testing
        self.db.create_tables()

        new_role = RoleEntity(
            name="1",
            description="1",
        )

        self.role_service.register_role(new_role)

        new_user = UserEntity(
            username="johndoe",
            fullname="John Doe",
            role_id=1,
        )

        self.user_service.register_user(new_user)

        retrieved_user = self.user_service.get(1)

        if retrieved_user:
            print(repr(retrieved_user))  # Output: Hi, John Doe

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()


def main() -> None:
    app_container = AppContainer()
    app_container.register_di()

    with App(app_container) as app:
        app.start()


if __name__ == "__main__":
    main()
