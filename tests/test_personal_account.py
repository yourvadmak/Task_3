from constants import BASE_URL
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    def test_navigate_to_personal_account(self, logged_in_driver):
        page = PersonalAccountPage(logged_in_driver)

        page.click_personal_account_link()

        assert page.is_account_page_opened(), (
            "Не произошёл переход в личный кабинет"
        )

    def test_navigate_to_order_history(self, logged_in_driver):
        page = PersonalAccountPage(logged_in_driver)
        page.click_personal_account_link()

        page.click_order_history_tab()

        assert page.is_order_history_page_opened(), (
            "Не произошёл переход в историю заказов"
        )

    def test_logout(self, logged_in_driver):
        page = PersonalAccountPage(logged_in_driver)
        page.click_personal_account_link()

        page.click_logout_button()

        assert page.is_login_page_opened(), (
            "После выхода не произошёл переход на страницу входа"
        )
        