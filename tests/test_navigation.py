import allure
import pytest
from pages.main_page import MainPage


class TestNavigation:

    @allure.title("Клик по логотипу Самоката возвращает на главную")
    def test_scooter_logo(self, driver):
        page = MainPage(driver)
        expected_url = driver.current_url
        page.click_order_top()
        page.wait_for_url_contains("/order")
        page.click_scooter_logo()
        assert page.get_home_page_url() == expected_url


    @allure.title("Клик по логотипу Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo(self, driver):
        page = MainPage(driver)
        original = page.get_current_window_handle()
        page.click_yandex_logo()
        page.wait_for_new_window()
        page.switch_to_new_window(original)
        assert "dzen" in page.get_current_url() or "ya.ru" in page.get_current_url()