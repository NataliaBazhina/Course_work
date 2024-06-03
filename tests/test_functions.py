from src.functions import get_operations


def test_get_operations():
#    assert get_operations('operations.json') == type(list)
    assert isinstance(get_operations('operations.json'), list)