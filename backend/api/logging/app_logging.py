import os.path
import logging
import os

import api.logging.config as config


LOGFILE = os.environ.get('logfile_path', './app_log.log')


class LoggingSetter:
    def __init__(self):
        self.logfile = LOGFILE
        self.logging_config = config.LOGGING_CONFIG
        assert (
            type(self.logging_config) == dict
        ), "Type of self.logging_config must be dictonary."

    def set_logger(self):
        # get logger configured with self,logging_config
        logging.config.dictConfig(self.logging_config)
