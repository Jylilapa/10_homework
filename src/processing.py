def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """Функция принимает список операций и возвращает список со статусом 'EXECUTED'"""

    return [i for i in operations if i.get("state") == state]


def sort_by_date(operations: list, reverse: bool = True) -> list:
    """Функция принимает список операций и возвращает отсортированный по дате список"""

    sort_operations_date = sorted(operations, key=lambda new_operations: new_operations["date"], reverse=reverse)
    return sort_operations_date
