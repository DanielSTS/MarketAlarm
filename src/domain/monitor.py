'''import time

from src.infra.database.repository import get_alarms_by_user


class MonitorService:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            alarms = get_alarms_by_user()
            for alarm in alarms:
                current_price = get_current_price(alarm.asset)
                if current_price >= alarm.target_price:
                    print(
                        f"Alarm triggered: Asset {alarm.asset} reached "
                        f"target price {alarm.target_price}"
                    )
            time.sleep(10)

    def stop(self):
        self.running = False


monitor_service = MonitorService()

if __name__ == "__main__":
    monitor_service.start()'''
