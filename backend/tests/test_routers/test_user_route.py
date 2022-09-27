from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

from backend.api.routers.user_route import user_login

from ...api.domains.user_model import UserCreate, UserDisplay, UserLogin
from ...api.infra.utils.pass_hassing import Hash
from ...api.main import app
from ..conftest import set_up_tear_down

app = app
client = TestClient(app)


@set_up_tear_down
def test_user_create(mocker):
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

    res = client.post("/server/users", json=jsonable_encoder(user))

    assert res.status_code == 200, res.json()

    content = res.json()

    assert content["username"] == user.username
    assert content["email"] == user.email


@set_up_tear_down
def test_user_login(mocker):
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

    res = client.post("/server/users", json=jsonable_encoder(user))

    assert res.status_code == 200, res.json()

    user_login = UserLogin(email=email, password=password)

    res = client.post("/server/users/login", json=jsonable_encoder(user_login))

    content = res.json()

    assert content["username"] == user.username
    assert content["email"] == user.email
    assert (
        Hash.verify_password(content["password"], user.password)
    ), user.password


@set_up_tear_down
def test_create_user_with_invalid_data(mocker):
    res = client.post("/server/users", json={})
    assert res.status_code == 422, res.json()
