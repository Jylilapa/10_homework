def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует часть номера карты"""

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскирует часть номеа счета"""

    return f"**{account_number[-4:]}"