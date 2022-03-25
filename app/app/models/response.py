import json
from pydantic import BaseModel
from typing import Optional


class Response(BaseModel):

    code: int = 200
    data: Optional[dict]

    def to_json(self, wrap: bool = False):
        return {
            "statusCode": self.code,
            "body": json.dumps(self.__body() if wrap else self.data),
        }

    def __body(self):
        return {"data": self.data}
