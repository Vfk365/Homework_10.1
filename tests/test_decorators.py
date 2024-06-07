from typing import Union

import pytest
from src.decorators import log


# Функция для тестирования
@log("test.log.txt")
def my_function(x: int, y: int) -> int:
    """Функция вызова декоратора с файлом сохранения test.log.txt"""
    return x + y


# Функция, которая вызывает ошибку
@log("test.log_error.txt")
def function_error(x: int, y: int) -> Union[int, float, None]:
    """Функция вызова декоратора с ошибкой и сохранения вывода в файл test.log_error.txt."""
    return x / y


# Тестирование успешного вызова функции
def test_log_decorator() -> None:
    result = my_function(2, 3)
    assert result == 5

    # Проверка лога
    with open("test.log.txt", "r") as file:
        log_contents = file.read()
    assert "function ok" in log_contents

    # Тестирование вызова функции с ошибкой
    with pytest.raises(ZeroDivisionError):
        function_error(2, 0)

    # Проверка лога ошибки
    with open("test.log_error.txt", "r") as file:
        log_contents = file.read()
    assert "function_error error" in log_contents
