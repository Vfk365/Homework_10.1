import csv
import os
from typing import Any

import pandas as pd
from src.logger import set_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "read_transactions_csv.log")
logger = set_logger("read_transactions_csv", file_path)


def get_data_transactions(path: str) -> Any:
    """Функция, которая принимает путь до файла и возвращает список словарей с данными"""
    try:
        logger.info("Открывает файл transactions.csv")
        with open(path, encoding="utf-8") as f:
            try:
                logger.info("Получение информации о транзакциях")
                reader = pd.read_csv(f, delimiter=";")
                # print(reader.shape)
                # print(reader.head(n))
                dict_trans = reader.to_dict(orient="records")

            except csv.Error as e:
                logger.error(f"Ошибка чтения CSV файла: {e}")
                return []
    except FileNotFoundError:
        logger.error("Путь к файлу transactions.csv не найден")
        return pd.DataFrame()

    return dict_trans
