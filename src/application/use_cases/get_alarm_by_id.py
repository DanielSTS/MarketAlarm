from src.application.use_cases.interfaces import AlarmDao


class GetAlarmById:
    def __init__(self, alarm_dao: AlarmDao):
        self.alarm_dao = alarm_dao

    def execute(self, id: str):
        alarm = self.alarm_dao.get_by_id(id)
        if not alarm:
            raise Exception("Alarm not found")
        return alarm
