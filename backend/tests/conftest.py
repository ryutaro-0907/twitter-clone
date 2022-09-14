import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database

from ..api.infra.db.base import Base
from ..api.infra.db.database import get_session
from ..api.main import app


@pytest.fixture(scope="function", name="test_session_local")
def fixture_test_session_local():
    """
    Set up test db session.
    delete db after tests.
    """
    test_sqlalchemy_database_url = "sqlite:///./test_temp.db"
    engine = create_engine(
        test_sqlalchemy_database_url, connect_args={"check_same_thread": False}
    )

    assert not database_exists(
        test_sqlalchemy_database_url
    ), "Test database already exists. Aborting tests."

    Base.metadata.create_all(engine)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    yield session_local

    drop_database(test_sqlalchemy_database_url)


def set_up_tear_down(f):
    def func(test_session_local, mocker, *args, **kwargs):

        def override_get_session():
            try:
                session = test_session_local()
                yield session
            finally:
                session.close()

        # initialize test db here if needed.

        app.dependency_overrides[get_session] = override_get_session

        f(mocker, *args, **kwargs)

        app.dependency_overrides[get_session] = get_session

    return func
