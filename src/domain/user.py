import uuid

from src.domain.bcrypt_password import BcryptPassword
from src.domain.email import Email


class User:
    def __init__(self, id: uuid.UUID, name: str, email: str, password: BcryptPassword):
        self.id = id
        self.name = name
        self.email: Email = Email(email)
        self.password = password

    @staticmethod
    def create(name: str, email: str, password: str) -> "User":
        return User(uuid.uuid4(), name, email, BcryptPassword.create(password))

    @staticmethod
    def restore(id: uuid.UUID, name: str, email: str, password: bytes, salt: bytes) -> "User":
        return User(id, name, email, BcryptPassword.restore(password, salt))

    def validate_password(self, password: str) -> bool:
        return self.password.validate(password)
