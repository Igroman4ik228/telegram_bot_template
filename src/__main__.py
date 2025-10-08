from app.services.user import UserCrudService
from container import AppContainer
from domain.models.user import UserOrm
from infrastructure.database.db import AlchemyDatabase


class App:
    def __init__(self, container: AppContainer):
        self.db = container.resolve(AlchemyDatabase)
        self.user_service = container.resolve(UserCrudService)

    def start(self) -> None:
        # Delete this after testing
        self.db.create_tables()

        new_user = UserOrm(
            first_name="John",
            last_name="Doe",
        )

        self.user_service.register_user(new_user)

        retrieved_user = self.user_service.get(1)
        if retrieved_user:
            print(retrieved_user.full_name)

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
