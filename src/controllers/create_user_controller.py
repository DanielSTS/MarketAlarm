from src.controllers.interfaces import HttpRequest, HttpResponse
from src.use_cases.create_user import CreateUser


class CreateUserController:
    def __init__(self, create_user: CreateUser):
        self.create_user = create_user

    def handle(self, request: HttpRequest) -> HttpResponse:
        name = request.body["name"]
        email = request.body["email"]
        password = request.body["password"]
        response = self.create_user.execute(name, email, password)
        return HttpResponse(status_code=201, body=response)
