import json
import os
from json import JSONDecodeError

path_to_file = os.path.join(os.path.dirname(__file__), "data", "operations.json")


def file_opening(path_to_file: str) -> list[dict]:
    """Функция принимает путь к JSON файлу и возвращает список словарей с транзакциями"""
    try:
        with open(path_to_file, encoding="utf-8") as file_json:
            try:
                transactions_info = json.load(file_json)
            except JSONDecodeError:
                transactions_info = []
                return transactions_info
        if not isinstance(transactions_info, list):
            return []
        return transactions_info
    except FileNotFoundError:
        transactions_info = []
        return transactions_info
