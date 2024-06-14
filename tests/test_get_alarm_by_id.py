import pytest

from src.application.use_cases.get_alarm_by_id import GetAlarmById


@pytest.fixture
def create_get_alarm_by_id_use_case(alarm_dao) -> GetAlarmById:
    return GetAlarmById(alarm_dao)


def test_get_alarm_existent(create_get_alarm_by_id_use_case, create_user_use_case, create_alarm_use_case):
    response_user = create_user_use_case.execute("John Doe", "john@example.com", "password123")
    response_alarm = create_alarm_use_case.execute(response_user['id'], "BTC", 50000.0)
    response = create_get_alarm_by_id_use_case.execute(response_alarm['id'])
    assert str(response.id) == response_alarm['id']
    assert str(response.user_id) == response_user['id']
    assert response.asset == "BTC"
    assert response.target_price == 50000.0


def test_get_alarm_not_found(create_get_alarm_by_id_use_case):
    with pytest.raises(Exception, match='Alarm not found'):
        create_get_alarm_by_id_use_case.execute("563a1434-5b99-4b76-b539-2dcd01ac4cc1")
