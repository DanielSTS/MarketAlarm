from src.controllers.interfaces import HttpRequest, HttpResponse
from src.use_cases.create_alarm import CreateAlarm


class CreateAlarmController:
    def __init__(self, create_alarm: CreateAlarm):
        self.create_alarm = create_alarm

    def handle(self, request: HttpRequest) -> HttpResponse:
        name = request.body["name"]
        email = request.body["email"]
        password = request.body["password"]
        response = self.create_alarm.execute(name, email, password)
        return HttpResponse(status_code=201, body=response)
