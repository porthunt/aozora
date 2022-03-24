from app.endpoints import endpoint


@endpoint()
def health(event, context):
    return {"message": "ok"}, 200
