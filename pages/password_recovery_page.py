import allure

from constants import BASE_URL
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators as Locators


class PasswordRecoveryPage(BasePage):

    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.driver.get(f"{BASE_URL}/login")

    @allure.step("Открыть страницу восстановления пароля")
    def open_forgot_password_page(self):
        self.driver.get(f"{BASE_URL}/forgot-password")

    @allure.step("Кликнуть по ссылке 'Восстановить пароль'")
    def click_restore_password_link(self):
        self.click(Locators.RESTORE_PASSWORD_LINK)

    @allure.step("Ввести email в поле восстановления пароля")
    def enter_email(self, email):
        self.send_keys(Locators.EMAIL_INPUT, email)

    @allure.step("Кликнуть по кнопке 'Восстановить'")
    def click_restore_button(self):
        self.click(Locators.RESTORE_BUTTON)

    @allure.step("Кликнуть по иконке показать/скрыть пароль")
    def click_show_password_icon(self):
        self.click(Locators.SHOW_PASSWORD_ICON)

    @allure.step("Проверить, что поле пароля подсвечено как активное")
    def is_password_field_active(self):
        wrapper = self.find_element(Locators.PASSWORD_WRAPPER)
        return "input_status_active" in wrapper.get_attribute("class")

    @allure.step("Проверить, что открыт адрес /forgot-password")
    def is_forgot_password_url_opened(self):
        return "/forgot-password" in self.get_current_url()
