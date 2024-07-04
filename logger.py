import logging


def set_logger():
    logger = logging.getLogger("utils")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler("../logs/utils.log", "w")
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger


def set_logger_masks():
    logger = logging.getLogger("masks")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler("../logs/masks.log", "w")
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger
