from src.masks import get_mask_account, get_mask_card


def mask_account_cart(number_string: str) -> str:
    """Функция получает строку и маскирует номер карты или счета"""
    if len(number_string.split()[-1]) == 16:
        new_number = get_mask_card(number_string.split()[-1])
        result = f"{number_string[:-16]}{new_number}"
        return result
    elif len(number_string.split()[-1]) == 20:
        new_number = get_mask_account(number_string.split()[-1])
        result = f"{number_string[:-20]}{new_number}"
    return result


def get_new_data(old_data: str) -> str:
    """Функция принимает строку даты и форматирует её"""
    data_slise = old_data[0:10].split("-")
    result = ".".join(data_slise[::-1])
    return result
