import pytest
import Task_2

@pytest.mark.smoke
def test_01_zero():
    assert Task_2.all_division(1, 0, 2, 3, 4, 5, 6, 7) is ZeroDivisionError

@pytest.mark.smoke
def test_02_correct():
    assert Task_2.all_division(1, 2, 3, 4, 5, 6) is not Exception

def test_03_type():
    assert Task_2.all_division(1, 3, 'a', -3, 4, 5, 6, 7) is TypeError

def test_04_empty():
    assert Task_2.all_division() is not IndexError

def test_05_negative_division():
    assert Task_2.all_division(-1, -2, 3, -4, 5) is not Exception