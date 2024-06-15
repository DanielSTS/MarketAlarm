class HttpRequest:

    def __init__(
        self,
        headers=None,
        body=None,
        query_params=None,
        path_params=None,
        url=None,
    ) -> None:
        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url


class HttpResponse:

    def __init__(self, status_code, body) -> None:
        self.status_code = status_code
        self.body = body
