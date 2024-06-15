from src.controllers.interfaces import HttpRequest, HttpResponse
from src.use_cases.get_alarm_by_id import GetAlarmById


class GetAlarmByIdController:
    def __init__(self, get_alarm_by_id: GetAlarmById):
        self.get_alarm_by_id = get_alarm_by_id

    def handle(self, request: HttpRequest) -> HttpResponse:
        id = request.body["id"]
        response = self.get_alarm_by_id.execute(id)
        return HttpResponse(status_code=200, body=response)
