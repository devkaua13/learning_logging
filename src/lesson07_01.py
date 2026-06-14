from typing import Any

LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers":False,
    "formatters": {
        "root_formatter":{
            "class": "logging.Formatter",
            "format": "[ ROOT:%(levelname)s] %(message)s",
        },
        "file_formatter":{
            "class": "logging.Formatter",
            "format": "()"
        },
        "stream_formatter":{
            "class": "logging.Formatter",
        },
    },
    "handlers":{},
    "filters": {},
    "root": {},
    "loggers": {},
    
}
