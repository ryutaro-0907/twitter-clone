from fastapi.testclient import TestClient
from ...api.main import app
from ...api.domains.user_model import UserCreate, UserDisplay

app = app
client = TestClient(app)


def test_user_login():
    username = "test user"
    email = "user@example.com"
    password = "password"
    created_at = "2020-01-01"
    updated_at = "2020-01-01"

    user = UserCreate(
        username=username,
        email=email,
        password=password,
        created_at=created_at,
        updated_at=updated_at,
    )

    response = client.get("/docs")
    assert response.status_code == 200, response.json()
    user_data = {
        "username": "test_user",
        "email": "test",
        "created_at": "string",
        "updated_at": "string",
        "deleted_at": "string",
        "password": "test",
    }

    response = client.post("/server/users", json=user_data)

    assert response.status_code == 200, response.json()

    assert isinstance(response.json(), UserDisplay) == True
