from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class MainPage(BasePage):

    ORDER_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    HOME_PAGE = (By.CLASS_NAME, "Home_HomePage__ZXKIX")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

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

    def click_order_top(self):
        self.click(self.ORDER_TOP)

    def click_order_bottom(self):
        self.click(self.ORDER_BOTTOM)

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

    def click_question(self, index):
        self.click(self.QUESTIONS[index])

    def get_answer(self, index):
        # Ждём именно видимости — accordion открывается с анимацией
        locator = (By.XPATH, f"//div[@id='accordion__panel-{index}']")
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text