import logging 
from typing import Any

from logging.config import dictConfig

LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers":False,
    "formatters": {
        "root_formatter":{
            "class": "logging.Formatter",
            "format": "[ DICT ROOT:%(levelname)s] %(message)s",
        },
        "file_formatter":{
            "class": "logging.Formatter",
            "format": "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d",
        },
        "stream_formatter":{
            "class": "logging.Formatter",
            "format": "[MEUAPP:%(levelname)s] %(message)s",
        },  
    },
    "handlers":{
        "root_stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "root_formatter",
            "stream": "ext://sys.stdout",
            "level": "WARNING",
        },

        "file_handler": {
            "class": "logging.FileHandler",
            "filename": "log.log",
            "mode": "w",
            "encoding": "utf-8",
            "formatter": "file_formatter",
        },

        "stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "stream_formatter",
            "stream": "ext://sys.stdout",
        }
    },
    "root": {
        "handlers": ["root_stream_handler"],
    },
    "loggers": {
        "meuapp": {
            "level": "DEBUG",
            "handlers": ["file_handler", "stream_handler"],
        },
    },
    
}

dictConfig(LOGGING_CONFIG)

logger = logging.getLogger("meuapp")

logger.debug("Mensagem de DEBUG")
logger.info("Mensagem de INFO")
logger.warning("Mensagem de WARNING")
logger.error("Mensagem de ERROR")
logger.critical("Mensagem de CRITICAL")
