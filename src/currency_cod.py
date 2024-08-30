import os

from src.logger import set_logger
from utils import data_transactions

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "currency_cod.log")
logger = set_logger("currency_cod", file_path)


def currency_cod_transaction(transactions, currency_cod):
    """вывод транзакции, содержащей заданную валюту"""

    logger.info("поиск транзакции, содержащей заданную валюту")
    try:
        my_transactions = []
        for transaction in transactions:
            try:
                if "operationAmount" in transaction:
                    # Проверка валюты
                    if transaction["operationAmount"]["currency"]["code"] == currency_cod:
                        logger.info("данный файл изначально был в формате JSON")
                        my_transactions.append(transaction)
                elif "currency_code" in transaction:
                    if transaction["currency_code"] == currency_cod:
                        logger.info("данный файл изначально  не был в формате JSON")
                        my_transactions.append(transaction)
                else:
                    logger.warning(f"Транзакция без нужных ключей: {transaction}")
            except Exception as e:
                logger.error(f"Неожиданная ошибка: {e} в транзакции: {transaction}")

        if my_transactions:
            return my_transactions
        else:
            return "Транзакций с такой валютой нет"

    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return "Произошла ошибка при поиске валюты транзакции"
