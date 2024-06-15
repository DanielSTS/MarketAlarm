from src.controllers.interfaces import HttpRequest, HttpResponse
from src.use_cases.get_alarms import GetAlarms


class GetAlarmsController:
    def __init__(self, get_alarms: GetAlarms):
        self.get_alarms = get_alarms

    def handle(self, request: HttpRequest) -> HttpResponse:
        user_id = request.body["id"]
        response = self.get_alarms.execute(user_id)
        return HttpResponse(status_code=200, body=response)
