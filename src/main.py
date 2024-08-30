import datetime
import os
from typing import Any

import pandas as pd
from src.processing import get_date_sorted, get_dictionary_key
from src.utils import data_transactions, filter_transactions_by_description, get_transactions_filter_by_rub
from src.widget import mask_account_cart


def main(file=None) -> Any:
    global transactions
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Введите номер пункта: ")

        if choice == "1":
            print("Для отработки выбран JSON-файл.")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "../data", "operations.json")
            transactions = data_transactions(file_path)
            break
        elif choice == "2":
            print("Для отработки выбран CSV-файл.")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "../data", "transactions.csv")
            transactions = data_transactions(file_path)
            break
        elif choice == "3":
            print("Для отработки выбран XLSX-файл.")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "../data", "transactions_exel.xlsx")
            transactions = data_transactions(file_path)
            break

        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        choice = input(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
        )
        if choice.upper() == "CANCELED":
            transactions = get_dictionary_key(transactions, "CANCELED")

            break
        if choice.upper() == "PENDING":
            transactions = get_dictionary_key(transactions, "PENDING")

            break
        if choice.upper() == "EXECUTED":
            transactions = get_dictionary_key(transactions)

            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        user_input = input("Отсортировать операции по дате? Да/Нет\n").lower()
        if user_input == "да":
            if (
                    input("Отсортировать по возрастанию или убыванию? по возрастанию/по убыванию\n").lower()
                    == "по возрастанию"
            ):
                transactions = get_date_sorted(transactions, False)
                break

            else:
                transactions = get_date_sorted(transactions)
                break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        user_input = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
        if user_input == "да":
             transactions = get_transactions_filter_by_rub(transactions, "RUB")
             break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

        while True:
            description_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет?").lower()
            if description_choice == "да":
                search_str = input("Введите слово для поиска в описании: ")
                transactions = filter_transactions_by_description(transactions.to_dict(orient="records"), search_str)

    print("Распечатываю итоговый список транзакций...")
    for transaction in transactions:
        date = datetime.datetime.fromisoformat(transaction["date"]).strftime("%d.%m.%Y")
        if "from" in transaction and (pd.notnull(transaction["from"]) or transaction["from"] != None):
            from_ = mask_account_cart(transaction["from"])
        else:
            from_ = "0"
        to_ = mask_account_cart(transaction["to"])
        description = transaction["description"]
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]
        print("Распечатываю итоговый список транзакций...")
        print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")


main()
