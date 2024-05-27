import functools
import sys
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор log, который логирует вызов функции и ёё результат в файл или консоль."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(message)
                else:
                    print(message, file=sys.stderr)
                return
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}, Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(message)
                else:
                    print(message, file=sys.stderr)
                raise

        return wrapper
    return decorator
