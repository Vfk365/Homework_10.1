import datetime
import os
from typing import Any
from src.processing import get_date_sorted, get_dictionary_key
from src.utils import data_transactions, filter_transactions_by_description, get_transactions_filter_by_rub
from src.widget import mask_account_cart


def main(file=None) -> Any:
    global transactions
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями. Пожалуйста, выберите файл для загрузки транзакций.")

    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Введите номер пункта: ")

        if choice == "1":
            print("Выбран JSON-файл.")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "../data", "operations.json")
            transactions = data_transactions(file_path)
            break
        elif choice == "2":
            print("Выбран CSV-файл.")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "../data", "transactions.csv")
            transactions = data_transactions(file_path)
            break
        elif choice == "3":
            print("Выбран XLSX-файл.")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "../data", "transactions_exel.xlsx")
            transactions = data_transactions(file_path)
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

    # Проверяем на пустую выборку
    if not transactions:
        print("Выборка транзакций пустая. Проверьте файл.")
        return

    while True:
        choice = input(
            "Введите статус для фильтрации (EXECUTED, CANCELED, PENDING):\n"
        ).upper()

        if choice in ["CANCELED", "PENDING", "EXECUTED"]:
            transactions = get_dictionary_key(transactions, choice)
            # Проверяем на пустую выборку после фильтрации
            if not transactions:
                print(f"Фильтр '{choice}' не вернул ни одной транзакции.")
                return
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

    while True:
        user_input = input("Отсортировать операции по дате? (Да/Нет)\n").lower()
        if user_input == "да":
            order = input("Сортировать по возрастанию или убыванию? (по возрастанию/по убыванию)\n").lower()
            if order == "по возрастанию":
                transactions = get_date_sorted(transactions, False)
            else:
                transactions = get_date_sorted(transactions)
            break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

    while True:
        user_input = input("Выводить только рублевые транзакции? (Да/Нет)\n").lower()
        if user_input == "да":
            transactions = get_transactions_filter_by_rub(transactions, "RUB")
            break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

    while True:
        description_choice = input(
            "Отфильтровать список транзакций по определенному слову в описании? (Да/Нет)\n").lower()
        if description_choice == "да":
            search_str = input("Введите слово для поиска в описании: ")
            transactions = filter_transactions_by_description(transactions.to_dict(orient="records"), search_str)
            break
        elif description_choice == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

    print("Распечатываю итоговый список транзакций...")
    for transaction in transactions:
        date = datetime.datetime.fromisoformat(transaction["date"]).strftime("%d.%m.%Y")
        from_ = mask_account_cart(transaction["from"]) if "from" in transaction and transaction["from"] else "0"
        to_ = mask_account_cart(transaction["to"])
        description = transaction["description"]
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]
        print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()