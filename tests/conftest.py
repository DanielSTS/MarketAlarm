import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.application.use_cases.create_alarm import CreateAlarm
from src.application.use_cases.create_user import CreateUser
from src.infra.database.alarm_dao import AlarmDaoDatabase
from src.infra.database.alarm_repository import AlarmRepositoryDatabase
from src.infra.database.models import Base
from src.infra.database.user_repository import UserRepositoryDatabase


@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(bind=engine)
    return engine


@pytest.fixture
def db_session(db_engine):
    session = sessionmaker(bind=db_engine)()
    Base.metadata.drop_all(bind=db_engine)
    Base.metadata.create_all(bind=db_engine)
    yield session
    session.rollback()
    session.close()
    Base.metadata.drop_all(bind=db_engine)


@pytest.fixture
def user_repository(db_session):
    return UserRepositoryDatabase(db_session)


@pytest.fixture
def alarm_repository(db_session):
    return AlarmRepositoryDatabase(db_session)


@pytest.fixture
def alarm_dao(db_session):
    return AlarmDaoDatabase(db_session)


@pytest.fixture
def create_user_use_case(user_repository) -> CreateUser:
    return CreateUser(user_repository)


@pytest.fixture
def create_alarm_use_case(user_repository, alarm_repository) -> CreateAlarm:
    return CreateAlarm(alarm_repository, user_repository)
