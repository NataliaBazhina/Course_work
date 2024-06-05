import pytest

from src.functions import get_operations, sort_data, date_prettify

@pytest.fixture
def mock_operations():
    ops = [
        {"state": "EXECUTED", "date": "2015-01-21T01:10:28.317704"},
        {"state": "CLOSED", "date": "2019-09-29T14:25:28.588059"},
        {"state": "EXECUTED", "date": "2028-01-21T01:10:28.317704"},
        {"state": "EXECUTED", "date": "2003-09-29T14:25:28.588059"},
        {"state": "EXECUTED", "date": "2016-01-21T01:10:28.317704"},

    ]
    return ops


def test_sort_data(mock_operations):
    """Проверяет сортировку списка по статусу и дате"""
    assert sort_data(mock_operations) == [
        {"state": "EXECUTED", "date": "2028-01-21T01:10:28.317704"},
        {"state": "EXECUTED", "date": "2016-01-21T01:10:28.317704"},
        {"state": "EXECUTED", "date": "2015-01-21T01:10:28.317704"},
        {"state": "EXECUTED", "date": "2003-09-29T14:25:28.588059"},

        ]

def test_get_operations():
    assert isinstance(get_operations('operations.json'), list)


def test_date_prettify():
    assert date_prettify("2028-01-21T01:10:28.317704") == "21.01.2028"
    assert date_prettify("2016-01-21T01:10:28.317704") == "21.01.2016"
