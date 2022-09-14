from ...api.domains.user_model import UserCreate


username = "test user"
email = "user@example.com"
password = "password"
created_at = "2020-01-01"
updated_at = "2020-01-01"


def test_user_create():
    user = UserCreate(
        username=username,
        email=email,
        password=password,
        created_at=created_at,
        updated_at=updated_at,
    )

    assert user.username == username
    assert user.email == email
    assert user.password == password
    assert user.created_at == created_at
    assert user.updated_at == updated_at
