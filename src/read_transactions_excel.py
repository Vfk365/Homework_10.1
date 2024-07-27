import os
from typing import Any

import pandas as pd
from src.logger import set_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "read_transactions_excel.log")
logger = set_logger("read_transactions_excel", file_path)


def get_data_transactions_excel(path: str) -> Any:
    try:
        logger.info(f"открытие файла {path}")
        df = pd.read_excel(path)
        logger.info("Получение информации о транзакциях")
        list_dict = df.to_dict(orient="records")
        return list_dict
    except FileNotFoundError:
        logger.error(f"путь к файлу {path} не найден")
        return "{}"
    except ValueError as e:
        logger.error(f"Ошибка при парсинге Excel файла: {str(e)}")
        return "{}"
