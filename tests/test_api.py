from fastapi.testclient import TestClient

from app.main import USERS, app

client = TestClient(app)


def setup_function():
    USERS.clear()


def test_health():
    response = client.get("/health")
    assert response.json() == {"status": "UP"}


def test_create_and_read():
    response = client.post(
        "/api/v1/users",
        json={"name": "Manoj", "email": "m@example.com"},
    )
    assert response.status_code == 201

    user_id = response.json()["id"]
    result = client.get(f"/api/v1/users/{user_id}")

    assert result.status_code == 200
    assert result.json()["email"] == "m@example.com"


def test_validation():
    response = client.post(
        "/api/v1/users",
        json={"name": "M", "email": "bad"},
    )
    assert response.status_code == 422


def test_missing():
    response = client.get("/api/v1/users/99999")
    assert response.status_code == 404
