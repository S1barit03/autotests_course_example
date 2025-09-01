# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome()
site_url = 'https://fix-online.sbis.ru/'

try:
    driver.get(site_url)
    driver.maximize_window()
    time.sleep(3)

    # авторизация
    user_login, user_password = 'ТестСергей2', 'Ntcn123!!'
    login_item = driver.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] [type="text"]')
    login_item.clear()
    login_item.send_keys(user_login)
    time.sleep(2)

    auth_item = driver.find_element(
        By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__checkSignInTypeButton"]'
    )
    auth_item.click()
    time.sleep(1)

    password_item = driver.find_element(By.CSS_SELECTOR,
                                        '[data-qa="auth-AdaptiveLoginForm__password"] [inputmode="text"]')
    password_item.clear()
    password_item.send_keys(user_password)
    time.sleep(2)

    auth_item = driver.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__signInButton"]')
    auth_item.click()
    time.sleep(6)

    # переход в раздел "Контакты"
    contacts_item = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    assert contacts_item.is_displayed(), 'Пункт перекрыт'
    time.sleep(3)
    contacts_item.click()
    time.sleep(3)
    sub_contacts_item = driver.find_element(By.CSS_SELECTOR,
                                            '[data-name="contacts"] .NavigationPanels-SubMenu__headTitle')
    sub_contacts_item.click()
    time.sleep(4)

    # открытие панели выбора сотрудника для нового сообщения
    plus_button_item = driver.find_element(By.CSS_SELECTOR, '[data-qa = "sabyPage-addButton"]')
    plus_button_item.click()
    time.sleep(4)

    # поиск текущего пользователя в панели сотрудников
    current_user = 'Супонев Сергей'
    search_line_item = driver.find_element(By.CSS_SELECTOR,
                                           '[data-qa = "controls-StackTemplate__headerContentTemplate"] [inputmode="search"]')
    search_line_item.clear()
    search_line_item.send_keys(current_user)
    time.sleep(3)

    result_employee = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    assert result_employee is not None, 'Результат поиска пустой'
    assert result_employee.text == current_user, 'Неверный результат поиска'

    result_employee.click()
    time.sleep(1)

    # ввод сообщения
    message_field_item = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    message_field_item.click()
    message_field_item.send_keys('Сообщение от Автотеста')

    # отправка письма
    send_item = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_item.click()
    time.sleep(2)

    # проверка появления сообщения в диалогах
    message_item = None
    table = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-workspace-detail [data-qa="item"]')
    for item in table:
        message_item = item.find_element(By.CSS_SELECTOR, '.msg-dialogs-item__message-text')
        # driver.execute_script("return arguments[0].scrollIntoView(true);", message_item)
        if message_item.text == 'Сообщение от Автотеста':
            break
    assert message_item and message_item.is_displayed(), 'Сообщение не отображается'
    time.sleep(2)

    # удаление сообщения
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message_item)
    action_chains.context_click(message_item)
    action_chains.perform()
    time.sleep(2)
    delete_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="cell"] [title="Перенести в удаленные"]')
    delete_button.click()
    time.sleep(2)

    # проверка, что сообщение удалено
    try:
        message_item.is_displayed()
    except StaleElementReferenceException:
        print('Удача')

finally:
    driver.quit()
