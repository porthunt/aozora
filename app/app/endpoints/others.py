from app.endpoints import endpoint
from app.models.response import Response


@endpoint()
def health(event, context):
    return Response(data={"status": "pass"})
