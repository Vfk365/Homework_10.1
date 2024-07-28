import json
import os
from typing import Dict, List

from src.logger import set_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = set_logger("utils", file_path_1)


def data_transactions(file_path: str) -> List[Dict]:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях."""
    logger.info("Запущена функция data_transactions")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            list_data_transactions = json.load(file)
            if isinstance(list_data_transactions, list):
                logger.info("Функция вернула список данных")
                return list_data_transactions
            else:
                logger.warning("Функция вернула пустой список данных")
                return []
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        logger.error(f"Ошибка {ex}")
        return []


transactions = data_transactions("../data/operations.json")
