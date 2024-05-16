from src.widget import mask_account_cart, get_new_data
from src.processing import get_dictionary_key, get_date_sorted


print(mask_account_cart("Visa Classic 6831982476737658"))

print(mask_account_cart("Счет 73654108430135874305"))

print(get_new_data("2018-07-11T02:26:18.671407"))

print(get_dictionary_key([{'id': "41428829", 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': "939719570", 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': "594226727", 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': "615064591", 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

print(get_date_sorted([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
