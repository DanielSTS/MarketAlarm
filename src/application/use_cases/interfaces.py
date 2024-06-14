from abc import ABC, abstractmethod
from src.domain.alarm import Alarm
from src.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: str) -> User:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass


class AlarmRepository(ABC):
    @abstractmethod
    def save(self, alarm: Alarm) -> None:
        pass


class AlarmDao(ABC):
    @abstractmethod
    def list_by_user_id(self, user_id: str) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id: str) -> None:
        pass
