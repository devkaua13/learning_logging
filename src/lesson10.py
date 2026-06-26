import config_logging
import logging

if __name__ == "__main__":
    config_logging.setup()
    
    logger = logging.getLogger('meuapp')

    logger.debug("Mensagem de debug")
    logger.info("Mensagem de info")
    logger.warning("Mensagem de warning")
    logger.error("Mensagem de error")
    logger.critical("Mensagem de critical")
