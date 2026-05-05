import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA


class TestOrder:

    @allure.title("Оформление заказа с данными: {data}")
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order(self, driver, data):
        main = MainPage(driver)
        main.click_order_top()
        order = OrderPage(driver)
        order.fill_first_form(data)
        order.fill_second_form()
        order.submit()
        assert order.is_success()