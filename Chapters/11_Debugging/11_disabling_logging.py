import logging

logging.basicConfig(
    level=logging.INFO, format=" %(asctime)s - %(levelname)s -  %(message)s"
)

logging.critical("Critical error! Critical error!")

logging.disable(logging.CRITICAL)  # disables all logging from this point onwards

logging.critical("Critical error! Critical error!")
logging.critical("Critical error! Critical error!")
