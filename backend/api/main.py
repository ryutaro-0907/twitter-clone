import logging
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import tweet_route, comment_route
from api.init_db import init

file_handler = logging.FileHandler(filename="app.log")
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
    handlers=handlers,
)

logger = logging.getLogger(__name__)
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
    init()
    logger.info("startup fisnihed successfully")


@app.on_event("shutdown")
def shutdown_event():
    logger.info("shutdown fisnihed successfully")
    # TODO add clean up  i.e. destroy development db


@app.get("/")
def hello_world():
    return "welcome to twitter clone server."


app.include_router(tweet_route.router, prefix="/api")
app.include_router(comment_route.router, prefix="/api")
