from fastapi.testclient import TestClient


def test_meta(test_client: TestClient) -> None:
    response = test_client.get("/api/meta", allow_redirects=False)
    assert response.json() == {"meta": {"app_version": "0.1.0"}, "error": {}}
    assert response.status_code == 200


def test_meta_trailing_slash(test_client: TestClient) -> None:
    response = test_client.get("/api/meta/", allow_redirects=False)
    assert response.json() == {"meta": {"app_version": "0.1.0"}, "error": {}}
    assert response.status_code == 200
