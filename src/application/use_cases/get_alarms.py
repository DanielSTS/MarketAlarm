from src.application.use_cases.interfaces import AlarmDao


class GetAlarms:
    def __init__(self, alarm_dao: AlarmDao):
        self.alarm_dao = alarm_dao

    def execute(self, user_id: str):
        return self.alarm_dao.list_by_user_id(user_id)
