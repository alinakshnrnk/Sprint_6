import pytest
from selenium import webdriver
from pages.main_page import MainPage

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    driver.maximize_window()
    main_page = MainPage(driver)
    main_page.dismiss_cookie()
    yield driver
    driver.quit()