import logging 
from logging.config import dictConfig
from typing import Any

# LOGGING_CONFIG: dict[str, Any] {
#   "vesion": 1, # sempre o mesmo valor
#   "disable_existing_loggers":False # Pra mim sempre o mesmo valor
#   "formatters": {} # Aqui vem nossos formatters
#   "handlers": {}, # Aqui vem os handlers
#   "filters": {}, # Aqui viriam os filters
#   "root": {} # Aqui vem as configurações do root
#   "loggers": {} # Aqui cada chave é um logger diferente
# }

# Dicionário de Configuração de Logging 
# A Configuração centralizada para o `dictConfig`
LOGGING_CONFIG: dict[str, Any] = {
    # Versão da configuração, sempre 1 por enquanto
    "version": 1,
    # 'False' para não desativar loggers das bibliotecas de terceiros
    'disable_existing_loggers': False,

    # Aqui vamos configurar o(s) Formatter(s)
    "formatters":{
        # A chave é o nome que você usa para se referir a esse formatter
        "main_formatter":{
            # As configs são `chave`: `valor` no dicionário
            # Aqui está nosso formato anterior 
            "format": "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d",
        },
        # Se tiver mais de um formatter, basta adicionar mais chaves com os nomes que você quiser
    },
    # Aqui já começa nossos Handlers
    "handlers":{
        # É sempre a mesma ideia, a chave é o nome do handler
        "file_handler":{
            "class": "logging.FileHandler",
            "filename": "../log.log",
            "mode": "a",
            "encoding": "utf-8",
            # Percebe-se o nome do Formatter que eu coloquei é a chave que eu criei lá no meu formatter
            "level": "DEBUG",
        },
        "stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "main_formatter",
            "level": "DEBUG",
        },
    },
    # ROOT CONFIG
    # Como o `root` é especial, tem uma chave somente para ele
    # Configuração  do logger raiz, que captura todos os logs.
    "root":{
        # Novamente, estou usando as chaves criadas em handlers 
        "handlers": ["file_handler", "stream_handler"],
    },
    # Aqui começa os loggers, apesar de que não precisamos disso
    # Vale ver como funciona
    'loggers':{
        "meuapp":{
            "level": "DEBUG",
        },
    },
}

dictConfig(LOGGING_CONFIG)

logger = logging.getLogger("meuapp")

logger.debug('testando o nível de debug')
logger.warning('testando a mensagem de warning')
logger.error('testando a mensagem de error')
