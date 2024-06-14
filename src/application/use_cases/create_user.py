from src.application.use_cases.interfaces import UserRepository
from src.domain.user import User


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, name: str, email: str, password: str):
        user = self.user_repository.get_by_email(email)
        if user:
            raise Exception("User already exists")
        user = User.create(name, email, password)
        self.user_repository.save(user)
        return {"id": str(user.id)}
