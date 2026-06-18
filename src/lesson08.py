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
                "%(taskName)s|%(operation)s"
            )   
        },

        "console":{
            "format": "%(message)s",
            "datefmt": "[%X]"},
    },

    "handlers":{

        "console":{
            "()": "rich.logging.RichHandler",
            "formatter": "console",
            "rich_tracebacks": False,
            "tracebacks_show_locals": False,
            "show_time": True,
            "show_level": True,
            "omit_repeated_times": True,
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


# Não utilizar fstring, pois com args podemos salvar os valores em tempo real no log
def dividir(x: float, y: float) -> float:
    logger.debug("Recebi x=%s e y=%s", x, y, extra={"operation": f"{x =} / {y =}"}
    )

    if y == 0:
        msg = f"Não posso dividir {x} por {y}"
        raise ZeroDivisionError(msg)

    resultado = x / y
    
    logger.info("O resultado da conta entre x=%s / y=%s = %s",x, y, resultado, extra={"operation": f"{x} / {y} = {resultado}"}
    )
    return resultado

if __name__ == '__main__':
    dividir(10, 5)


#    try:
#        dividir(10, 0)
#    except ZeroDivisionError:
#        logger.exception("Divisao por 0")
