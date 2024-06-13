def test_register(client):
    response = client.post(
        "/register", json={"username": "test_user", "password": "test_password"}
    )
    assert response.status_code == 201
    assert response.json == {"user_id": 1, "username": "test_user"}


def test_register_existing_username(client):
    client.post(
        "/register", json={"username": "test_user", "password": "test_password"}
    )
    response = client.post(
        "/register", json={"username": "test_user", "password": "test_password"}
    )
    assert response.status_code == 409
    assert response.json == {"error": "Username already exists"}


def test_create_alarm(client):
    response = client.post(
        "/alarms",
        json={"asset": "BTC", "target_price": 50000.0},
        headers={"Authorization": "Bearer test_token"},
    )
    assert response.status_code == 201
    assert response.json == {"alarm_id": 1, "asset": "BTC", "target_price": 50000.0}


def test_get_alarms(client):
    response = client.get("/alarms", headers={"Authorization": "Bearer test_token"})
    assert response.status_code == 200
    assert response.json == {"alarms": []}
