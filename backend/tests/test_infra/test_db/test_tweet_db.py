from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder

from backend.api.routers.tweet_route import create_tweet

from ....api.main import app
from ....api.domains.tweet_model import InputTweet, Tweet
from ....api.infra.db.tweet_db import TweetDBHandler
from ...conftest import set_up_tear_down


app = app
client = TestClient(app)


@set_up_tear_down
def test_create_tweet(mocker):
    handler = TweetDBHandler(mocker)
    assert handler is not None