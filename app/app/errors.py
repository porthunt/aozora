from app.settings import logger


class Error(Exception):

    default_message = ""

    def __init__(self, message=None, error_id=None, **kwargs):
        Exception.__init__(self)
        self.message = (
            message if message else self.default_message.format(**kwargs)
        )
        self.status = "error"
        self.error_id = error_id if error_id else None
        self.content = self.content if hasattr(self, "content") else True
        self.log_error = self.log_error if hasattr(self, "log_error") else True
        if self.log_error:
            logger.error(self.message)

    def __str__(self):
        return self.message

    def to_json(self):
        if not self.content:
            return None

        response = {
            "message": self.message,
            "status_code": self.status_code,
            "status": self.status,
        }
        if self.error_id:
            response["id"] = self.error_id
        return response


class UnexpectedError(Error):
    status_code = 500
    default_message = "Unexpected error"
