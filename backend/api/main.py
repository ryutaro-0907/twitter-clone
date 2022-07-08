import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.logging.app_logging import LoggingSetter
from api.routers import tweet_route
from api.init_db import init


setter = LoggingSetter()
setter.set_logger()
logger = logging.getLogger(__name__)
logger.info("session starts.")

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup_event():
    pass
    logger.info("startup started")
    init()
    logger.info('startup fisnihed successfully')

# @app.on_event("shutdown")
# def shutdown_event():
#     logger.info('shutdown fisnihed successfully')
#     # TODO add clean up methods

@app.get('/')
def hello_world():
    return 'welcome to twitter clone server.'


app.include_router(tweet_route.router, prefix="/api")
