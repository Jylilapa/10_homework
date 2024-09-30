import re
from collections import Counter


def operations_search(transactions: list[dict], search_string: str) -> list[dict]:
    """Функция принимает на вход список транзакций и строку поиска и возвращает список транзакций,
    в описании которых содержится искомая строка"""
    pattern = re.compile(search_string, re.IGNORECASE)
    operations_filter = []
    for transaction in transactions:
        if re.search(pattern, transaction["description"]):
            operations_filter.append(transaction)
    return operations_filter


def count_description(transactions: list[dict], categories: list) -> dict:
    """Функция принимает на вход список транзакций и список категорий и возвращает словарь,
    где ключи это описание операций, а значения это количество операций в каждой категории
    """
    categories_dict = []
    for transaction in transactions:
        descript = transaction["description"]
        for category in categories:
            if re.search(category, descript, re.IGNORECASE):
                categories_dict.append(category)
    counted_description = Counter(categories_dict)
    return counted_description


print(operations_search([
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }], "Перевод организации"))
