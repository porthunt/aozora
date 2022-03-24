import json
import uuid
from functools import wraps
from app.settings import logger
from app.errors import Error, UnexpectedError


def endpoint():
    def decorator(function, *args):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                event = args[0]
                _args = [event, *args[1:]]
                body, status_code = function(*_args)
            except Exception as e:
                error_id = str(uuid.uuid4())
                logger.exception(error_id)
                if not issubclass(e.__class__, Error):
                    e = UnexpectedError(
                        message="Unexpected error", error_id=error_id
                    )
                body = e.to_json()
                status_code = e.status_code
            return {
                "statusCode": status_code,
                "body": json.dumps(body),
            }

        return wrapper

    return decorator
