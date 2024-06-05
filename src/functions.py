import json


def get_operations(name):
    with open(name) as f:
        return json.load(f)





def sort_data(operations: list) -> list:
    """
    Принимает неотсортированный список операций клиента
    Выводит список успешных операций, сортированных по дате
    """
    dict_operation = []
    for element in operations:
        if 'date' not in element.keys() or 'from' not in element.keys() or 'to' not in element.keys():
            continue
        if element not in dict_operation and element.get('state', None) == "EXECUTED":
            dict_operation.append(element)

    return sorted(dict_operation, key=lambda data: data["date"], reverse=True)[:5]


def date_prettify(date: str) -> str:
    """
    Получает дату из списка
    Выводит преобразованную дату в виде ДД.ММ.ГГГГ
    """
    date_new = date[0:10].split('-')
    date_new = ".".join(ch for ch in reversed(date_new))
    return date_new


def secure(payment_number: str) -> str:
    """
    Получает информацию откуда и куда совершен перевод
    Вывод преобразованную информацию в формате:
    номер карты XXXX XX** **** XXXX; номер счета **XXXX
    """
    from_data_split = payment_number.split(' ')
    num = from_data_split[-1]
    if from_data_split[0] == 'Счет':
        return f'{from_data_split[0]} **{num[-4:]}'

    if from_data_split[0] == 'Visa':
        return f'{from_data_split[0]} {from_data_split[1]} {num[0:4]} {num[4:6]}** **** {num[-4:]}'

    return f'{from_data_split[0]} {num[0:4]} {num[4:6]}** **** {num[-4:]}'
