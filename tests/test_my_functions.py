import pytest

import source.my_functions as my_functions


def test_add():
    assert my_functions.add(1, 2) == 3
    
def test_add_string():
    result = my_functions.add('Hello', 'World')
    assert result == 'HelloWorld'
    
def test_divide():
    assert my_functions.divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(5, 0)