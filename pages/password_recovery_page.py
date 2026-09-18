from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators as Locators


class PasswordRecoveryPage(BasePage):
    def click_restore_password_link(self):
        self.click(Locators.RESTORE_PASSWORD_LINK)

    def enter_email(self, email):
        self.send_keys(Locators.EMAIL_INPUT, email)

    def click_restore_button(self):
        self.click(Locators.RESTORE_BUTTON)

    def click_show_password_icon(self):
        self.click(Locators.SHOW_PASSWORD_ICON)

    def is_password_field_active(self):
        wrapper = self.find_element(Locators.PASSWORD_WRAPPER)
        return "input_status_active" in wrapper.get_attribute("class")

    def is_forgot_password_url_opened(self):
        return "/forgot-password" in self.get_current_url()
    