from datetime import datetime

from src.application.use_cases.interfaces import UserRepository
from src.domain.token_generator import TokenGenerator


class Login:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str):
        user = self.user_repository.get_by_email(email)
        if user and user.validate_password(password):
            token = TokenGenerator.sign(user, datetime.now())
            return {
                'token': token,
                'id': user.id
            }
        else:
            raise Exception('Invalid credentials')
