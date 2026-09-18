from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager

GECKODRIVER_PATH = "/Users/vadmin/.wdm/drivers/geckodriver/mac64/v0.37.1/geckodriver"


class WebDriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service)
        elif browser_name == "firefox":
            service = FirefoxService(GECKODRIVER_PATH)
            return webdriver.Firefox(service=service)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        