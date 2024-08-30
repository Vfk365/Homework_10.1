import os
import re
from collections import Counter

from src.logger import set_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "categories_description.log")
logger = set_logger("categories_description", file_path)


def list_categories(transactions):

    return (transaction["description"] for transaction in transactions if "description" in transaction)


def categories_by_descriptions(my_list_categories):

    counted = Counter(my_list_categories)
    return counted


def description_transaction(transactions, my_string):
    """вывод транзакции, содержащей заданное описание"""
    logger.info("поиск транзакции, содержащей заданное описание")
    try:
        pattern = re.compile(rf"{re.escape(my_string)}", re.IGNORECASE)
        my_transactions = []
        for transaction in transactions:
            try:
                if pattern.search(transaction["description"]):
                    logger.debug(f"Найдено совпадение в транзакции: {transaction['id']}")
                    my_transactions.append(transaction)

            except KeyError as ke:
                logger.error(f"Ошибка KeyError: {ke} в транзакции: {transaction}")
            except Exception as e:
                logger.error(f"Неожиданная ошибка: {e} в транзакции: {transaction}")

        if my_transactions:
            return my_transactions
        else:
            return "Такого описания нет"

    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return "Произошла ошибка при поиске описания"
