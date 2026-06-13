import logging 

format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"

logging.basicConfig(
    level = logging.ERROR,
    format = format1,
    filename = "../log.log",
    filemode = "a",
    encoding = "utf-8",
)

logger = logging.getLogger("meuapp")


logger.error("Marina")
logger.debug("Essa bosta que vai aparecer no arquivo quando rodar")
logger.warning("Marina eu te amo")
logger.info("Kaua danado")
logger.critical("fodase")
