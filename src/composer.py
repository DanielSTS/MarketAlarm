from src.controllers.create_alarm_controller import CreateAlarmController
from src.controllers.create_user_controller import CreateUserController
from src.controllers.get_alarm_by_id_controller import GetAlarmByIdController
from src.controllers.get_alarms_controller import GetAlarmsController
from src.controllers.login_controller import LoginController
from src.infra.database.alarm_dao import AlarmDaoDatabase
from src.infra.database.alarm_repository import AlarmRepositoryDatabase
from src.infra.database.user_repository import UserRepositoryDatabase
from src.use_cases.create_alarm import CreateAlarm
from src.use_cases.create_user import CreateUser
from src.use_cases.get_alarm_by_id import GetAlarmById
from src.use_cases.get_alarms import GetAlarms
from src.use_cases.login import Login
from src.infra.database.connection import db_session


def create_user_composer():
    user_repository = UserRepositoryDatabase(db_session)
    use_case = CreateUser(user_repository)
    return CreateUserController(use_case).handle


def create_alarm_composer():
    user_repository = UserRepositoryDatabase(db_session)
    alarm_repository = AlarmRepositoryDatabase(db_session)
    use_case = CreateAlarm(alarm_repository, user_repository)
    return CreateAlarmController(use_case).handle


def login_composer():
    user_repository = UserRepositoryDatabase(db_session)
    use_case = Login(user_repository)
    return LoginController(use_case).handle


def get_alarm_by_id_composer():
    alarm_dao = AlarmDaoDatabase(db_session)
    use_case = GetAlarmById(alarm_dao)
    return GetAlarmByIdController(use_case).handle


def get_alarms_composer():
    alarm_dao = AlarmDaoDatabase(db_session)
    use_case = GetAlarms(alarm_dao)
    return GetAlarmsController(use_case).handle
