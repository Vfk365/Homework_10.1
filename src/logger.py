import logging
import os
from typing import Any


def set_logger(name: str, logs_file: str) -> Any:
    """Функция логирования"""
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(logs_file, mode="w")
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger
