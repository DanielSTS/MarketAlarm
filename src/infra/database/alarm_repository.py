from sqlalchemy.orm import Session

from src.domain.alarm import Alarm
from src.infra.database.models import AlarmModel
from src.use_cases.interfaces import AlarmRepository


class AlarmRepositoryDatabase(AlarmRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, alarm: Alarm) -> None:
        alarm_model = self.entity_to_model(alarm)
        self.db.add(alarm_model)
        self.db.commit()

    @staticmethod
    def entity_to_model(entity: Alarm) -> AlarmModel:
        return AlarmModel(
            id=entity.id,
            user_id=entity.user_id,
            asset=entity.asset,
            target_price=entity.target_price,
        )
