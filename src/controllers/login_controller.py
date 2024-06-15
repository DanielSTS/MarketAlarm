from src.controllers.interfaces import HttpRequest, HttpResponse
from src.use_cases.login import Login


class LoginController:
    def __init__(self, login: Login):
        self.login = login

    def handle(self, request: HttpRequest) -> HttpResponse:
        email = request.body["email"]
        password = request.body["password"]
        response = self.login.execute(email, password)
        return HttpResponse(status_code=200, body=response)
