from src.application.use_cases.interfaces import AlarmRepository, UserRepository
from src.domain.alarm import Alarm


class CreateAlarm:
    def __init__(self, alarm_repository: AlarmRepository, user_repository: UserRepository):
        self.alarm_repository = alarm_repository
        self.user_repository = user_repository

    def execute(self, user_id: str, asset: str, target_price: float):
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise Exception('User not found')
        alarm = Alarm.create(user.id, asset, target_price)
        self.alarm_repository.save(alarm)
        return {
            'id': str(alarm.id)
        }
