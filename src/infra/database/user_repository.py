import uuid

from sqlalchemy.orm import Session

from src.domain.user import User
from src.infra.database.models import UserModel
from src.use_cases.interfaces import UserRepository


class UserRepositoryDatabase(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, id: str):
        user_id = uuid.UUID(id)
        user_model = self.db.query(UserModel).filter_by(id=user_id).first()
        if user_model:
            return self.model_to_entity(user_model)

    def get_by_email(self, email: str) -> User:
        user_model = self.db.query(UserModel).filter_by(email=email).first()
        if user_model:
            return self.model_to_entity(user_model)

    def save(self, user: User) -> None:
        user_model = self.entity_to_model(user)
        self.db.add(user_model)
        self.db.commit()

    @staticmethod
    def model_to_entity(model: UserModel) -> User:
        return User.restore(
            id=model.id,
            name=model.name,
            email=model.email,
            password=model.password_hash,
            salt=model.password_salt,
        )

    @staticmethod
    def entity_to_model(entity: User) -> UserModel:
        return UserModel(
            id=entity.id,
            name=entity.name,
            email=entity.email.value,
            password_hash=entity.password.value,
            password_salt=entity.password.salt,
        )
