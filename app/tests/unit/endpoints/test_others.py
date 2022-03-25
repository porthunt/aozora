import json
from app.endpoints.others import health
from tests.unit.endpoints import fake_event


def test_health():
    r = health(fake_event, None)
    assert r["statusCode"] == 200
    assert json.loads(r["body"]) == {"status": "pass"}
