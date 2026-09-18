from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators as Locators


class PersonalAccountPage(BasePage):
    def click_personal_account_link(self):
        self.click(Locators.PERSONAL_ACCOUNT_LINK)

    def click_order_history_tab(self):
        self.click(Locators.ORDER_HISTORY_TAB)

    def click_logout_button(self):
        self.click(Locators.LOGOUT_BUTTON)

    def is_account_page_opened(self):
        return self.wait_for_url_contains("/account")

    def is_order_history_page_opened(self):
        return self.wait_for_url_contains("/account/order-history")

    def is_login_page_opened(self):
        return self.wait_for_url_contains("/login")
    