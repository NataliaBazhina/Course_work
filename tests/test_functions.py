import pytest

from src.functions import get_operations, sort_data, date_prettify, secure


@pytest.fixture
def mock_operations():
    ops = [
        {
            "id": 154927927,
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614",
            "operationAmount": {
                "amount": "30153.72",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Maestro 7810846596785568",
            "to": "Счет 43241152692663622869",
        },
        {
            "id": 114832369,
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890",
            "operationAmount": {
                "amount": "48150.39",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Visa Classic 2842878893689012",
            "to": "Счет 35158586384610753655",
        },
        {
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {
                "amount": "62814.53",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125",
        },
        {
            "id": 509645757,
            "state": "EXECUTED",
            "date": "2019-10-30T01:49:52.939296",
            "operationAmount": {
                "amount": "23036.03",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 7756673469642839",
            "to": "Счет 48943806953649539453",
        },
        {
            "id": 888407131,
            "state": "EXECUTED",
            "date": "2019-09-29T14:25:28.588059",
            "operationAmount": {
                "amount": "45849.53",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 35421428450077339637",
            "to": "Счет 46723050671868944961",
        },
    ]
    return ops




def test_sort_data(mock_operations):
    """Проверяет сортировку списка по статусу и дате"""
    assert sort_data(mock_operations) == [
        {
            "id": 114832369,
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890",
            "operationAmount": {
                "amount": "48150.39",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Visa Classic 2842878893689012",
            "to": "Счет 35158586384610753655",
        },
        {
            "id": 154927927,
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614",
            "operationAmount": {
                "amount": "30153.72",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Maestro 7810846596785568",
            "to": "Счет 43241152692663622869",
        },
        {
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {
                "amount": "62814.53",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125",
        },
        {
            "id": 509645757,
            "state": "EXECUTED",
            "date": "2019-10-30T01:49:52.939296",
            "operationAmount": {
                "amount": "23036.03",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 7756673469642839",
            "to": "Счет 48943806953649539453",
        },
        {
            "id": 888407131,
            "state": "EXECUTED",
            "date": "2019-09-29T14:25:28.588059",
            "operationAmount": {
                "amount": "45849.53",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 35421428450077339637",
            "to": "Счет 46723050671868944961",
        },
    ]


def test_get_operations():
    assert isinstance(get_operations('operations.json'), list)


def test_date_prettify():
    assert date_prettify("2028-01-21T01:10:28.317704") == "21.01.2028"
    assert date_prettify("2016-01-21T01:10:28.317704") == "21.01.2016"

def test_secure():
    assert secure("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert secure("Visa Classic 2842870027279012") == "Visa Classic 2842 87** **** 9012"
    assert secure("Счет 44812258784861134719") == "Счет **4719"
