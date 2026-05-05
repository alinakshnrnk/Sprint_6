import allure
import pytest
from pages.main_page import MainPage
from data.faq_data import EXPECTED_TEXTS


class TestFaq:

    @allure.title("Проверка ответа на вопрос {index}")
    @pytest.mark.parametrize("index, expected", list(enumerate(EXPECTED_TEXTS)))
    def test_faq(self, driver, index, expected):
        page = MainPage(driver)
        page.click_question(index)
        assert page.get_answer(index) == expected