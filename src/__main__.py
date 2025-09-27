from app.services.crud.user import UserCrudService
from domain.entities.user import UserEntity
from infrastructure.database.db import AlchemyDatabase
from infrastructure.database.uow import AlchemyUoW


def main() -> None:
    db = AlchemyDatabase()
    db.create_tables()

    user_service = UserCrudService(AlchemyUoW(db.session_maker))

    new_user = UserEntity(username="johndoe", fullname="John Doe")
    user_service.register_user(new_user)

    retrieved_user = user_service.get(1)
    if retrieved_user:
        print(repr(retrieved_user))  # Output: Hi, John Doe


if __name__ == "__main__":
    main()
