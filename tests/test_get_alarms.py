import pytest

from src.use_cases.get_alarms import GetAlarms


@pytest.fixture
def create_get_alarms_use_case(alarm_dao) -> GetAlarms:
    return GetAlarms(alarm_dao)


def test_get_alarms(
    create_get_alarms_use_case, create_user_use_case, create_alarm_use_case
):
    response_user = create_user_use_case.execute(
        "John Doe", "john@example.com", "password123"
    )
    user_id = response_user["id"]
    response_alarm1 = create_alarm_use_case.execute(user_id, "BTC", 10.1)
    response_alarm2 = create_alarm_use_case.execute(user_id, "ETH", 20.2)
    response = create_get_alarms_use_case.execute(user_id)
    assert str(response[0].id) == response_alarm1["id"]
    assert str(response[0].user_id) == user_id
    assert response[0].asset == "BTC"
    assert response[0].target_price == 10.1
    assert str(response[1].id) == response_alarm2["id"]
    assert str(response[1].user_id) == user_id
    assert response[1].asset == "ETH"
    assert response[1].target_price == 20.2
