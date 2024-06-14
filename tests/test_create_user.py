import uuid

import pytest
from src.application.use_cases.create_alarm import CreateAlarm
from src.application.use_cases.create_user import CreateUser


@pytest.fixture
def create_alarm_use_case(user_repository, alarm_repository) -> CreateAlarm:
    return CreateAlarm(alarm_repository, user_repository)


@pytest.fixture
def create_user_use_case(user_repository) -> CreateUser:
    return CreateUser(user_repository)


def test_create_user_success(create_user_use_case):
    response = create_user_use_case.execute(
        "John Doe", "john@example.com", "password123"
    )
    assert uuid.UUID(response["id"])


def test_create_existent_user(create_user_use_case):
    create_user_use_case.execute("John Doe", "john@example.com", "password123")
    with pytest.raises(Exception, match="User already exists"):
        create_user_use_case.execute("John Doe", "john@example.com", "password123")
