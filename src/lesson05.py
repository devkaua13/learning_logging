import logging 

format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"

logging.basicConfig(
    level = logging.DEBUG,
    format = format1,
    filename = "../log.log",
    filemode = "a",
    encoding = "utf-8",
)

logger = logging.getLogger("meuapp")

logger.debug("Essa bosta que vai aparecer no arquivo quando rodar")
