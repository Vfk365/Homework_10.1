import json
import os
import re
from typing import Dict, List

from src.logger import set_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = set_logger("utils", file_path_1)


def filter_transactions_by_description(transactions, search_string):
    """
    Фильтрует список транзакций по строке поиска в описании.

    :param transactions: Список словарей с транзакциями.
    :param search_string: Строка для поиска в поле 'description'.
    :return: Список словарей, содержащих строки, соответствующие поисковому запросу.
    """
    filtered_transactions = [
        transaction
        for transaction in transactions
        if re.search(search_string, transaction.get("description", ""), re.IGNORECASE)
    ]
    return filtered_transactions


def count_transactions_by_category(transactions, categories):
    """
    Подсчитывает количество транзакций по категориям.

    :param transactions: Список словарей с транзакциями.
    :param categories: Список категорий для подсчета.
    :return: Словарь с количеством операций по категориям.
    """
    category_count = {category: 0 for category in categories}

    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1

    return category_count


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


def get_transactions_filter_by_rub(transactions: list, search_key: str) -> list:
    """Функция фильтрации транзакций по коду валюты"""
    result = []
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and re.search(search_key, transaction["operationAmount"]["currency"]["code"], re.IGNORECASE)
        ):
            result.append(transaction)
    return result
