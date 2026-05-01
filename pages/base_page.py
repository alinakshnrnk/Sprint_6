import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def dismiss_cookie(self):
        try:
            btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.COOKIE_BUTTON)
            )
            btn.click()
        except Exception:
            pass

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click(self, locator):
        element = self.find(locator)
        self.scroll_to(element)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def write(self, locator, text):
        self.find(locator).send_keys(text)

    def wait_for_url_contains(self, part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(part)
        )

    def wait_for_new_window(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(2)
        )

    def switch_to_new_window(self, original_handle):
        for handle in self.driver.window_handles:
            if handle != original_handle:
                self.driver.switch_to.window(handle)
                break

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window_handle(self):
        return self.driver.current_window_handle