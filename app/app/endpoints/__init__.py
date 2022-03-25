import uuid
from functools import wraps
from app.settings import logger
from app.errors import Error, UnexpectedError
from app.models.response import Response


def endpoint():
    def decorator(function, *args):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                event = args[0]
                _args = [event, *args[1:]]
                response = function(*_args)
            except Exception as e:
                error_id = str(uuid.uuid4())
                logger.exception(error_id)
                if not issubclass(e.__class__, Error):
                    e = UnexpectedError(
                        message="Unexpected error", error_id=error_id
                    )
                response = Response(code=e.status_code, data=e.to_json())
            return response.to_json()

        return wrapper

    return decorator
