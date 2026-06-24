import logging 
from typing import Any

from logging.config import dictConfig
from rich.console import Console
import sys

console_stdout = Console(file=sys.stdout)
console_stderr = Console(file=sys.stderr)


LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers":False,
    "formatters": {

        "file":{
            "class": "logging.Formatter",
            "format": (
                "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"
                "|%(funcName)s|%(module)s|%(process)d|%(processName)s|%(thread)d|%(threadName)s"
                "%(taskName)s"
            )   
        },

        "console_stderr":{"format": "ERR: %(message)s", "datefmt": "[%X]"},

        "console_stdout":{"format": "OUT: %(message)s", "datefmt": "[%X]"},
    },

    "handlers":{

        "console_stdout":{
            "()": "handlers.MyRichHandler",
            "formatter": "console_stdout",
            "rich_tracebacks": False,
            "tracebacks_show_locals": False,
            "show_time": True,
            "show_level": True,
            "omit_repeated_times": True,
            "markup": False,
            "enable_link_path": True,
            "show_path": True,
            "file": "stdout",
        },

        "console_stderr":{
            "()": "handlers.MyRichHandler",
            "formatter": "console_stderr",
            "rich_tracebacks": False,
            "tracebacks_show_locals": False,
            "show_time": True,
            "show_level": True,
            "omit_repeated_times": True,
            "markup": False,
            "enable_link_path": True,
            "show_path": True,
            "file": "stderr",
        },
         
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file",
            "filename": "log.log",
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "encoding": "utf-8",
        },
    },

    "root": {
        "handlers": ["console_stdout", "console_stderr", "file"]
    },
    "loggers": {
        "meuapp": {
            "level": "DEBUG",
        },
    }, 
}

dictConfig(LOGGING_CONFIG)

logger = logging.getLogger("meuapp")


if __name__ == '__main__':
    logger.debug("Mensagem de debug")
    logger.info("Mensagem de info")
    logger.warning("Mensagem de warning")
    logger.error("Mensagem de error")
    logger.critical("Mensagem de critical")
