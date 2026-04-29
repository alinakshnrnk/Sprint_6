import pytest
from selenium import webdriver
from pages.base_page import BasePage

BASE_URL = "https://qa-scooter.praktikum-services.ru/"  # поменяй на свой URL

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    driver.maximize_window()

    # Закрываем баннер один раз для всего теста
    BasePage(driver).dismiss_cookie()

    yield driver
    driver.quit()