# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest
import Task_2

@pytest.mark.parametrize('result', [(1, 0, 2, 3, 4, 5, 6, 7),
                                    pytest.param((1, 2, 3, 4, 5, 6), marks=pytest.mark.smoke),
                                    (1, 3, 'a', -3, 4, 5, 6, 7),
                                    pytest.param((), marks=pytest.mark.skip('скип по заданию')),
                                    (-1, -2, 3, -4, 5)],
                         ids=['zero', 'correct', 'type', 'empty', 'negative_division'])
def test_params(result):
    assert Task_2.all_division(*result) is not Exception