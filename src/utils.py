import json
import os
from typing import Dict, List


def data_transactions(file_path: str) -> List[Dict]:
    '''Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.'''
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            list_data_transactions = json.load(file)
            if isinstance(list_data_transactions, list):
                return list_data_transactions
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


transactions = data_transactions("../data/operations.json")
