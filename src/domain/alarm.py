import uuid


class Alarm:
    def __init__(self, id: uuid.UUID, user_id: uuid.UUID, asset: str, target_price: float):
        self.id = id
        self.user_id = user_id
        self.asset = asset
        self.target_price = target_price

    @staticmethod
    def create(user_id: uuid.UUID, asset: str, target_price: float) -> "Alarm":
        return Alarm(uuid.uuid4(), user_id, asset, target_price)
