import logging 
from typing import Any

from logging.config import dictConfig

LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers":False,
    "formatters": {

        "file":{
            "class": "logging.Formatter",
            "format": (
                "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"
                "|%(funcName)s|%(module)s|%(process)d|%(processName)s|%(thread)d|%(threadName)s"
                "%(taskName)s|"
            )   
        },

        "console":{
            "format": "%(message)s",
            "datefmt": "%H:%M:%S"},
    },

    "handlers":{

        "console":{
            "()": "rich.logging.RichHandler",
            "formatter": "console",
            "rich_tracebacks": True,
            "tracebacks_show_locals": True,
            "show_time": True,
            "show_level": True,
            "omit_repeated_times": False,
            "markup": False,
            "enable_link_path": True,
            "show_path": True,
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
        "handlers": ["console", "file"]
    },
    "loggers": {
        "meuapp": {
            "level": "DEBUG",
        },
    }, 
}

dictConfig(LOGGING_CONFIG)

logger = logging.getLogger("meuapp")

def dividir(x: float, y: float) -> float:
    logger.debug(f"Recebi x={x} e y={y}")

    if y == 0:
        msg = f"Não posso dividir {x} por {y}"
        raise ZeroDivisionError(msg)

    resultado = x / y
    logger.info(f"O resultado é {resultado}")
    return resultado

if __name__ == '__main__':
    dividir(10, 5)
