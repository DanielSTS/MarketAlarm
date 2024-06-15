from werkzeug.exceptions import HTTPException

from src.controllers.interfaces import HttpResponse


def error_handler(ex: Exception) -> HttpResponse:
    if isinstance(ex, HTTPException):
        return HttpResponse(
            status_code=ex.code,
            body={
                "error": {"code": ex.code, "message": ex.name, "detail": ex.description}
            },
        )

    return HttpResponse(
        status_code=500,
        body={"error": {"code": 500, "message": "Internal Server Error"}},
    )
