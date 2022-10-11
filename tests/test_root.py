from fastapi.testclient import TestClient


def test_root(test_client: TestClient) -> None:
    response = test_client.get("/", allow_redirects=False)
    assert response.json() == {"message": "Welcome to the Users Microservice."}
    assert response.status_code == 200
