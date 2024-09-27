from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
join_path_csv = BASE_DIR / "data" / "transactions.csv"
join_path_exc = BASE_DIR / "data" / "transactions_excel.xlsx"


def transaction_read_csv(join_path_csv):
    """Функция принимает на вход путь до файла csv и возвращает список словарей с транзакциями"""
    try:
        transaction_csv = pd.read_csv(join_path_csv)
        return transaction_csv
    except FileNotFoundError:
        transactions = []
        return transactions


def transaction_read_exsel(join_path_exc):
    """Функция принимает на вход путь до файла escel и возвращает список словарей с транзакциями"""
    try:
        transaction_excel = pd.read_csv(join_path_exc)
        return transaction_excel
    except FileNotFoundError:
        transactions = []
        return transactions


print(transaction_read_csv(join_path_csv))
print(transaction_read_exsel(join_path_exc))
