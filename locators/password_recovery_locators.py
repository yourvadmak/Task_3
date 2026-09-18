from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    EMAIL_INPUT = (By.NAME, "name")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_ICON = (By.CLASS_NAME, "input__icon-action")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    PASSWORD_WRAPPER = (By.XPATH, "//div[contains(@class, 'input__icon-action')]/..")