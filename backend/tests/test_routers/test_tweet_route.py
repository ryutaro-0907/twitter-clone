from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

from backend.api.routers.tweet_route import create_tweet

from ...api.domains.tweet_model import InputTweet, Tweet
from ...api.infra.utils.pass_hassing import Hash
from ...api.main import app
from ..conftest import set_up_tear_down

app = app
client = TestClient(app)


@set_up_tear_down
def test_user_create(mocker):
    username = "test user"
    user_id = 1
    text = 'test text'

    tweet = InputTweet(
        user_id=user_id,
        username=username,
        text=text
    )

    res = client.post("/server/tweets", json=jsonable_encoder(tweet))

    assert res.status_code == 200, res.json()

    content = res.json()

    assert content["username"] == tweet.username
    assert content["text"] == tweet.text
