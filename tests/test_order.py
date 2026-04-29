import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA

@pytest.mark.parametrize("data", ORDER_DATA)
def test_order(driver, data):
    main = MainPage(driver)
    main.click_order_top()

    order = OrderPage(driver)
    
    order.fill_first_form(data)
    
    # Добавим выбор метро, если это требуется (пример):
    # order.select_metro("Киевская")
    
    order.fill_second_form()
    order.submit()

    assert order.is_success()