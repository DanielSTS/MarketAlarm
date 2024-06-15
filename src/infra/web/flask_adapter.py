from typing import Callable

from flask import request

from src.controllers.interfaces import HttpRequest, HttpResponse


def request_adapter(req: request, controller: Callable) -> HttpResponse:
    body = None
    if req.data:
        body = req.json
    http_request = HttpRequest(
        body=body,
        headers=req.headers,
        query_params=req.args,
        path_params=req.view_args,
        url=req.full_path,
    )
    http_response = controller(http_request)
    return http_response
