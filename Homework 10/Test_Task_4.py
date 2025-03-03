# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import Task_2

class TestsHomework:

    def test_zero(self, start_time):
        assert Task_2.all_division(1, 0, 2, 3, 4, 5, 6, 7) is not ZeroDivisionError

    def test_correct(self, during_time):
        assert Task_2.all_division(range(1,10)) is not Exception