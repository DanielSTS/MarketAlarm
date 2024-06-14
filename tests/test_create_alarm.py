import uuid

import pytest


def test_create_alarm_success(create_alarm_use_case, create_user_use_case):
    response = create_user_use_case.execute("John Doe", "john@example.com", "password123")
    asset = "BTC"
    target_price = 50000.0
    alarm = create_alarm_use_case.execute(response['id'], asset, target_price)
    assert uuid.UUID(alarm['id'])


def test_create_alarm_user_not_found(create_alarm_use_case):
    user_id = "563a1434-5b99-4b76-b539-2dcd01ac4cc1"
    asset = "BTC"
    target_price = 50000.0
    with pytest.raises(Exception, match='User not found'):
        create_alarm_use_case.execute(user_id, asset, target_price)
