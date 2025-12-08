import logging
from logging.handlers import RotatingFileHandler
import os

LOG_PATH = "log"
LOG_FILE = "app.log"

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)


def setup_logger():
    logger = logging.getLogger("backend logger")
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        f"{LOG_PATH}/{LOG_PATH}", maxBytes=2000, backupCount=3
    )

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
