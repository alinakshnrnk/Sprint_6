from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class OrderPage(BasePage):

    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[contains(@placeholder,'Адрес')]")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[@class='select-search__select']//div")
    PHONE = (By.XPATH, "//input[contains(@placeholder,'Телефон')]")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_OPTION = (By.XPATH, "//div[text()='сутки']")

    COLOR_BLACK = (By.ID, "black")

    ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle__1CSJM') and text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    SUCCESS = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    def fill_first_form(self, data):
        self.write(self.NAME, data["name"])
        self.write(self.LASTNAME, data["lastname"])
        self.write(self.ADDRESS, data["address"])

        # Ввод метро: вводим текст, ждём список, кликаем первый вариант
        self.write(self.METRO_INPUT, data.get("metro", "Киевская"))
        first_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.METRO_OPTION)
        )
        first_option.click()

        self.write(self.PHONE, data["phone"])
        self.click(self.NEXT_BUTTON)

    def fill_second_form(self):
        tomorrow = datetime.now() + timedelta(days=1)
        day = str(tomorrow.day)  # например "25", без нулей
        
        self.click(self.DATE)
        
        # XPath: ищем день в текущем месяце, не outside-month
        date_locator = (By.XPATH,
            f"//div[contains(@class,'react-datepicker__day') "
            f"and not(contains(@class,'outside-month')) "
            f"and not(contains(@class,'disabled')) "
            f"and normalize-space(text())='{day}']"
        )
        self.click(date_locator)

        self.click(self.RENT)
        self.click(self.RENT_OPTION)
        self.click(self.COLOR_BLACK)

    def submit(self):
        self.click(self.ORDER_BUTTON)
        self.click(self.YES_BUTTON)

    def is_success(self):
        return self.find_visible(self.SUCCESS).is_displayed()