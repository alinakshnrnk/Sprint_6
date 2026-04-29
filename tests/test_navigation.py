from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_scooter_logo(driver):
    page = MainPage(driver)
    page.click_order_top()
    # Ожидаем перехода на страницу заказа
    WebDriverWait(driver, 10).until(EC.url_contains("/order"))
    page.click_scooter_logo()
    # Проверяем возврат на главную по наличию уникального элемента
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "Home_Header__iJKdX"))
    )

def test_yandex_logo(driver):
    page = MainPage(driver)
    # Сохраняем текущее окно
    original_window = driver.current_window_handle
    # Открываем ссылку в новом окне/вкладке
    page.click_yandex_logo()
    # Ожидаем появления второго окна
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    # Переходим в новое окно (не по индексу, а исключая исходное)
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break
    # Проверяем, что URL содержит ожидаемые домены
    assert any(x in driver.current_url for x in ["dzen", "ya.ru"])