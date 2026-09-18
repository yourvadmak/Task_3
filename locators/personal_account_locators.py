from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDER_HISTORY_TAB = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    