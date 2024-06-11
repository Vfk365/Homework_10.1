import json
from typing import List, Dict
import os


def data_transactions(file_path: str) -> List[Dict]:
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
