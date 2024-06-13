from src.infra.db.repository import get_user_by_username


def authenticate(username, password):
    user = get_user_by_username(username)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload["identity"]
    return get_user_by_username(user_id)
