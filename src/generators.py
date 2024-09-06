def filter_by_currency(transaction_list, name):
    new_list_transactions = list(filter(lambda transaction_list: name==(transaction_list.get("operationAmount").get("currency").get("name")), transaction_list))
    return new_list_transactions


def transaction_descriptions(transactions):
    transactions_info = list(map(lambda transactions: transactions.get("description"), transactions))
    for transaction in transactions_info:
        # transaction_str = str(transaction)
        yield transaction


def card_number_generator(start: int, end: int) -> str:
    for number in range(start, end+1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = '0' + card_number

        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

        yield (formatted_card_number)


gen_number = card_number_generator(1,3)
print(next(gen_number))
print(next(gen_number))
print(next(gen_number))