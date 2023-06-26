import time
from app.db.repository import get_alarms_by_user

class MonitorService:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            alarms = get_alarms_by_user()  # Obtenha os alarmes do banco de dados
            for alarm in alarms:
                # Lógica de monitoramento da cotação e verificação de alarmes disparados
                # Você pode usar uma biblioteca externa para obter as cotações em tempo real
                # ou acessar uma API de cotação como o Alpha Vantage, por exemplo
                current_price = get_current_price(alarm.asset)
                if current_price >= alarm.target_price:
                    print(f"Alarm triggered: Asset {alarm.asset} reached target price {alarm.target_price}")
                    # Aqui você pode adicionar a lógica para notificar o usuário (por exemplo, enviar um e-mail)

            time.sleep(10)  # Aguarde 10 segundos antes de verificar novamente

    def stop(self):
        self.running = False

monitor_service = MonitorService()

if __name__ == '__main__':
    monitor_service.start()
