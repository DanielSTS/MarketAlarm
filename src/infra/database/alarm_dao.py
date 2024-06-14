import uuid

from sqlalchemy.orm import Session
from src.application.use_cases.interfaces import AlarmDao
from src.infra.database.models import AlarmModel


class AlarmDaoDatabase(AlarmDao):

    def __init__(self, db: Session):
        self.db = db

    def list_by_user_id(self, user_id: str):
        id = uuid.UUID(user_id)
        return self.db.query(AlarmModel).filter_by(user_id=id)

    def get_by_id(self, id: str) -> None:
        alarm_id = uuid.UUID(id)
        return self.db.query(AlarmModel).filter_by(id=alarm_id).first()
