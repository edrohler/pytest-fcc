import pytest
import time

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
        
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10,5)
    assert result == 2
    
@pytest.mark.skip(reason='Not implemented yet.')
def test_multiply():
    assert my_functions.multiply(2, 3) == 6
    
@pytest.mark.xfail(reason='Not implemented yet.')
def test_subtract():
    assert my_functions.subtract(5, 2) == 3