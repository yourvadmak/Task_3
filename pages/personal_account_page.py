import allure

from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators as Locators


class PersonalAccountPage(BasePage):

    @allure.step("Кликнуть по ссылке 'Личный Кабинет' в шапке")
    def click_personal_account_link(self):
        self.click(Locators.PERSONAL_ACCOUNT_LINK)

    @allure.step("Кликнуть по вкладке 'История заказов'")
    def click_order_history_tab(self):
        self.click(Locators.ORDER_HISTORY_TAB)

    @allure.step("Кликнуть по кнопке 'Выход'")
    def click_logout_button(self):
        self.click(Locators.LOGOUT_BUTTON)

    @allure.step("Проверить, что открыт раздел личного кабинета")
    def is_account_page_opened(self):
        return self.wait_for_url_contains("/account")

    @allure.step("Проверить, что открыта страница истории заказов")
    def is_order_history_page_opened(self):
        return self.wait_for_url_contains("/account/order-history")

    @allure.step("Проверить, что открыта страница входа")
    def is_login_page_opened(self):
        return self.wait_for_url_contains("/login")
    