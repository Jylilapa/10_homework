import logging


# Создаем основные конфигурации logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    filename="masks.log",
    filemode="w",
    encoding="utf-8",
)
# Создаем логи для отдельных функций
card_number_logger = logging.getLogger("app.card_number")
mask_account_logger = logging.getLogger("app.mask_account")


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует часть номера карты"""
    card_number_logger.info("Ввод номера карты")
    if len(card_number) < 16:
        card_number_logger.error("Недостаточное количество цифр")
        return "Ошибка: проверьте количество вводимых цифр"
    else:
        mask_card_number = (
            f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        )
    card_number_logger.info("Маскировка номера карты")
    return mask_card_number


print(get_mask_card_number("7000792289606361"))
print(get_mask_card_number("70007922896"))


def get_mask_account(account_number: str) -> str:
    """Функция маскирует часть номеа счета"""
    mask_account_logger.info("Ввод номера счета")
    if len(account_number) < 20:
        mask_account_logger.error("Недостаточное количество цифр")
        return "Ошибка: проверьте количество вводимых цифр"
    else:
        mask_account = f"**{account_number[-4:]}"
        mask_account_logger.info("Маскировка номера счета")
    return mask_account


print(get_mask_account("73654108430135874305"))
print(get_mask_account("7365410843013587"))
