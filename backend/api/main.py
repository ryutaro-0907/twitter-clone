import logging
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import tweet_route, comment_route, user_route
from api.init_db import insert_initial_data_to_db, clear_db

from logging.config import dictConfig
import logging
from .settings import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger('app_logger')
logger.info("session starts.")

app = FastAPI()

origins = ["*"]

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
    return "welcome to twitter clone app server. For reference please go to /docs"

app.include_router(user_route.router, prefix="/server")
app.include_router(tweet_route.router, prefix="/server")
app.include_router(comment_route.router, prefix="/server")
