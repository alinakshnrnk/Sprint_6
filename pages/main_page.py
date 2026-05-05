import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class MainPage(BasePage):

    ORDER_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    HOME_PAGE = (By.CLASS_NAME, "Home_HomePage__ZXKIX")

    QUESTIONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]

    ANSWERS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]

    @allure.step("Нажать кнопку Заказать вверху страницы")
    def click_order_top(self):
        self.click(self.ORDER_TOP)

    @allure.step("Нажать кнопку Заказать внизу страницы")
    def click_order_bottom(self):
        self.click(self.ORDER_BOTTOM)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

    @allure.step("Нажать на вопрос с индексом {index}")
    def click_question(self, index):
        self.click(self.QUESTIONS[index])

    @allure.step("Получить текст ответа с индексом {index}")
    def get_answer(self, index):
        return self.find_visible(self.ANSWERS[index]).text

    @allure.step("Дождаться главной страницы")
    def wait_for_home_page(self):
        self.find_visible(self.HOME_PAGE)
    
    @allure.step("Получить текущий URL")
    def get_home_page_url(self):
        self.find_visible(self.HOME_PAGE)
        return self.get_current_url()