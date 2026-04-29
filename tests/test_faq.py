import pytest
from pages.main_page import MainPage


EXPECTED_TEXTS = [
    "Сутки — 400 рублей",
    "один заказ — один самокат",
    "Допустим, вы оформляете заказ",
    "начиная с завтрашнего дня",
    "Пока что нет",
    "Самокат приезжает",
    "Да, пока самокат не привезли",
    "Да, обязательно"
]


@pytest.mark.parametrize("index, expected", list(enumerate(EXPECTED_TEXTS)))
def test_faq(driver, index, expected):
    page = MainPage(driver)
    page.click_question(index)
    text = page.get_answer(index)
    assert expected in text