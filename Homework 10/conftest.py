import pytest
import datetime
import time

@pytest.fixture(scope='class')
def start_time():
    yield print("Время старта: \n", datetime.datetime.now())
    print("Время завершения: \n", datetime.datetime.now())

@pytest.fixture(scope='function')
def during_time():
    start = time.time()
    yield start
    end = time.time()
    print("\nВремя выполнения: \n", round((end - start), 10))