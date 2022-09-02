"""conftest."""
import uuid

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database


@pytest.fixture(scope="function", name="test_session_local")
def fixture_test_session_local():
    """Test Session."""
    # settings of test database
    test_sqlalchemy_database_url = "sqlite:///./test_temp.db"
    engine = create_engine(
        test_sqlalchemy_database_url, connect_args={"check_same_thread": False}
    )

    assert not database_exists(
        test_sqlalchemy_database_url
    ), "Test database already exists. Aborting tests."

    # Create test database and tables
    entities.Base.metadata.create_all(engine)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Run the tests
    yield session_local

    # Drop the test database
    drop_database(test_sqlalchemy_database_url)


def set_up_tear_down(f):
    """Temp db."""

    def func(test_session_local, mocker, *args, **kwargs):
        # テスト用のDBに接続するためのsessionmaker instanse
        #  (SessionLocal) をfixtureから受け取る

        def override_get_db():
            try:
                db = test_session_local()
                yield db
            finally:
                db.close()

        init_test_db(test_session_local)

        # fixtureから受け取るSessionLocalを使うようにget_dbを強制的に変更
        app.dependency_overrides[get_db] = override_get_db
        app.dependency_overrides[get_file_io] = override_get_file_io
        app.dependency_overrides[get_current_user] = override_get_current_user

        app.dependency_overrides[get_file_io] = override_get_file_io
        app.dependency_overrides[get_current_user] = override_get_current_user

        # Run tests
        # import pdb
        # pdb.set_trace()
        f(mocker, *args, **kwargs)
        # 元に戻す
        app.dependency_overrides[get_db] = get_db
        app.dependency_overrides[get_file_io] = get_file_io
        app.dependency_overrides[get_current_user] = get_current_user

    return func


def async_set_up_tear_down(f):
    """Temp db (for async)."""

    async def func(test_session_local, mocker, *args, **kwargs):
        # テスト用のDBに接続するためのsessionmaker instanse
        #  (SessionLocal) をfixtureから受け取る

        def override_get_db():
            try:
                db = test_session_local()
                yield db
            finally:
                db.close()

        init_test_db(test_session_local)

        # fixtureから受け取るSessionLocalを使うようにget_dbを強制的に変更
        app.dependency_overrides[get_db] = override_get_db
        app.dependency_overrides[get_file_io] = override_get_file_io
        app.dependency_overrides[get_current_user] = override_get_current_user

        # Run tests
        await f(mocker, *args, **kwargs)
        # 元に戻す
        app.dependency_overrides[get_db] = get_db
        app.dependency_overrides[get_file_io] = get_file_io
        app.dependency_overrides[get_current_user] = get_current_user

    return func


def init_test_db(test_session_local):
    """Initialize DB."""
    with test_session_local() as db:
        organization_datasource.create_organization(
            db=db, code=OrganizationCode("hacarus"), name=OrganizationName("株式会社○○")
        )
