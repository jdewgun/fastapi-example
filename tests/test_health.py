from fastapi.testclient import TestClient


def test_health(test_client: TestClient) -> None:
    response = test_client.get("/api/health", allow_redirects=False)
    assert response.status_code == 200
    assert response.json() == {"health": "stable", "error": {}}


def test_health_trailing_slash(test_client: TestClient) -> None:
    response = test_client.get("/api/health/", allow_redirects=False)
    assert response.status_code == 200
    assert response.json() == {"health": "stable", "error": {}}
