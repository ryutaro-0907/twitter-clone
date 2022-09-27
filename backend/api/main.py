import logging
from logging.config import dictConfig

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .init_db import clear_db, insert_initial_data_to_db
from .routers import (comment_route, presigned_url_route, tweet_route,
                      user_route)
from .settings import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("app_logger")
logger.info("session starts.")


origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    pass
    logger.info("startup started")
    insert_initial_data_to_db()
    logger.info("startup fisnihed successfully")


@app.on_event("shutdown")
def shutdown_event():
    logger.info("shutdown fisnihed successfully")
    clear_db()
    # TODO add clean up  i.e. destroy development db


@app.get("/")
def hello_world():
    return "welcome to twitter clone app server. For reference please go to http://0.0.0.0:8000/docs"


app.include_router(user_route.router, prefix="/server")
app.include_router(tweet_route.router, prefix="/server")
app.include_router(comment_route.router, prefix="/server")
app.include_router(presigned_url_route.router, prefix="/server")


class APPTaker:
    app: FastAPI = app
