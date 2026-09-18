from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def wait_for_url_contains(self, url_part, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))
            return True
        except Exception:
            return False

    def wait_for_elements_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return True
        except Exception:
            return False

    def wait_for_text_not_equal(self, locator, excluded_text, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.find_element(*locator).text != excluded_text
            )
            return True
        except Exception:
            return False

    def get_current_url(self):
        return self.driver.current_url