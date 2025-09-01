# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get('https://sbis.ru/')
    driver.maximize_window()
    time.sleep(3)
    assert driver.current_url == 'https://saby.ru/', 'Неверно открыт сайт'

    contacts_item = driver.find_element(By.CSS_SELECTOR, '.sbis_ru-Header__menu-link')
    driver.execute_script("return arguments[0].scrollIntoView(true);", contacts_item)
    contacts_item.click()
    time.sleep(3)

    driver.get('https://tensor.ru/')
    time.sleep(3)
    assert driver.current_url == 'https://tensor.ru/', 'Неверно открыт сайт'

    block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg')
    driver.execute_script("return arguments[0].scrollIntoView(true);", block)
    time.sleep(3)
    assert block.is_displayed(), 'Силы в людях нет'

    about = block.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__link')
    about.click()
    assert driver.current_url == 'https://tensor.ru/about', 'Неверно открыт сайт'
    time.sleep(3)

finally:
    driver.quit()