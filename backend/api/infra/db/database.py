"""Database settings."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.infra.db.base import Base

# if os.environ.get('DB_TYPE') == 'sqlite':
#     SQLALCHEMY_DATABASE_URL = "sqlite:///./twitter_app.db"

# elif os.environ.get('DB_TYPE') == 'postgres':
db_user = os.environ.get('DB_USER', 'user')
db_pass = os.environ.get('DB_PASS', 'pass')
db_endpoint = os.environ.get('DB_ENDPOINT', 'development-db:5432')

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_endpoint}/app_db"
# SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Initialize DB."""
    with SessionLocal() as db:
       raise NotImplementedError

def get_session():
    """Get DB Session."""
    with SessionLocal() as session:
        yield session
