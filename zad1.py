import logging

def get_logs(level, format_string):
    logging.basicConfig(level=level, format=format_string)
    return logging

logger = get_logs(logging.DEBUG, '%(asctime)s - %(levelname)s - %(message)s')
logger.debug("Debugujesz kod")
logger.info("Informacja = dobre jedzenie")
logger.error("Wystąpił błąd")
logger.warning("Uwaga ktoś wchodzi!")
