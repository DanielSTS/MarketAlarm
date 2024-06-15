from datetime import datetime

import jwt

from src.domain.user import User


class TokenGenerator:
    EXPIRES_IN = 1000000
    KEY = "secret"

    @staticmethod
    def sign(user: User, date: datetime) -> str:
        payload = {
            "email": user.email.value,
            "iat": date.timestamp(),
            "expiresIn": TokenGenerator.EXPIRES_IN,
        }
        return jwt.encode(payload, TokenGenerator.KEY, algorithm="HS256")

    @staticmethod
    def verify(token: str) -> dict:
        return jwt.decode(token, TokenGenerator.KEY, algorithms=["HS256"])
