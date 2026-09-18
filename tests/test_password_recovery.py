from constants import BASE_URL
from pages.password_recovery_page import PasswordRecoveryPage
from locators.password_recovery_locators import PasswordRecoveryLocators as Locators


class TestPasswordRecovery:
    def test_navigate_to_password_recovery_page(self, driver):
        driver.get(f"{BASE_URL}/login")
        page = PasswordRecoveryPage(driver)

        page.click_restore_password_link()

        assert page.is_forgot_password_url_opened(), (
            "Не произошёл переход на страницу восстановления пароля"
        )

    def test_enter_email_and_click_restore(self, driver):
        driver.get(f"{BASE_URL}/forgot-password")
        page = PasswordRecoveryPage(driver)

        page.enter_email("test@example.com")
        page.click_restore_button()

        assert page.is_element_visible(Locators.PASSWORD_INPUT), (
            "После клика на 'Восстановить' не появилось поле пароля"
        )

    def test_show_password_icon_activates_field(self, driver):
        driver.get(f"{BASE_URL}/forgot-password")
        page = PasswordRecoveryPage(driver)
        page.enter_email("test@example.com")
        page.click_restore_button()

        page.click_show_password_icon()

        assert page.is_password_field_active(), (
            "Поле пароля не подсветилось после клика на иконку показать/скрыть"
        )
        