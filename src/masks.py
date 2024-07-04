from logger import set_logger_masks

logger = set_logger_masks()


def get_mask_card(number: str) -> str:
    """Функция принимает строку и возвращает маску карты"""
    logger.info("Запущена функция get_mask_card")
    new_string = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    logger.info("Функция вернула замаскированный номер карты")
    return new_string


def get_mask_account(number: str) -> str:
    """Функция принимает строку и возвращает маску счёта"""
    logger.info("Запущена функция get_mask_account")
    new_string = f"**{number[-4:]}"
    logger.info("Функция вернула замаскированный номер счёта")
    return new_string


result = get_mask_card("123456789101")
result = get_mask_account("12345621859856789101")
