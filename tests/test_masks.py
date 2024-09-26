from src.masks import get_mask_account, get_mask_card_number


def tests_get_mask_card_number() -> None:
    """Тест на проверку маскировки номера карты"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def tests_get_mask_card_number_error() -> None:
    assert (
        get_mask_card_number("7000792289606")
        == "Ошибка: проверьте количество вводимых цифр"
    )


def tests_get_mask_account() -> None:
    """Тест на проверку маскировки номера счета"""
    assert get_mask_account("73654108430135874305") == "**4305"


def tests_get_mask_account_error() -> None:
    assert (
        get_mask_account("7365410843013587")
        == "Ошибка: проверьте количество вводимых цифр"
    )
