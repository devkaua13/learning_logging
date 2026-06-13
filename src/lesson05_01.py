import logging
import sys

format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"

# Podemos criar nossos próprios handlers usando as classes que foram mencionadas antes
file_handler = logging.FileHandler(
    filename = '../log.log',
    mode = 'a',
    encoding = 'utf-8',
)

stream_handler = logging.StreamHandler(sys.stdout)

# Nossos Handlers precisam de Formatters
main_formatter = logging.Formatter(fmt=format1)

# A configuração do formatter pode ser reutilizada
file_handler.setFormatter(main_formatter)
stream_handler.setFormatter(main_formatter)


