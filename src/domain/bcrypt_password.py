import bcrypt


class BcryptPassword:
    def __init__(self, value: bytes, salt: bytes):
        self.value = value
        self.salt = salt

    @staticmethod
    def create(password: str) -> "BcryptPassword":
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return BcryptPassword(hashed_password, salt)

    @staticmethod
    def restore(value: bytes, salt: bytes) -> "BcryptPassword":
        return BcryptPassword(value, salt)

    def validate(self, password: str) -> bool:
        hashed_password = self.value
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
