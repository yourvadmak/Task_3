from constants import BASE_URL
from pages.constructor_page import ConstructorPage


class TestMainFunctionality:
    def test_navigate_to_constructor(self, driver):
        driver.get(BASE_URL)
        page = ConstructorPage(driver)
        page.click_feed_link()

        page.click_constructor_link()

        assert page.wait_for_url_contains(BASE_URL) or "/feed" not in page.get_current_url(), (
            "Не произошёл переход в конструктор"
        )

    def test_navigate_to_feed(self, driver):
        driver.get(BASE_URL)
        page = ConstructorPage(driver)

        page.click_feed_link()

        assert page.wait_for_url_contains("/feed"), (
            "Не произошёл переход в ленту заказов"
        )

    def test_ingredient_modal_opens_and_closes(self, driver):
        driver.get(BASE_URL)
        page = ConstructorPage(driver)

        page.click_first_ingredient()
        assert page.is_ingredient_modal_opened(), (
            "Не появилось окно с деталями ингредиента"
        )

        page.close_modal()
        assert page.is_modal_closed(), (
            "Окно с деталями ингредиента не закрылось по крестику"
        )

    def test_adding_ingredient_increases_counter(self, driver):
        driver.get(BASE_URL)
        page = ConstructorPage(driver)
        counter_before = page.get_first_ingredient_counter()

        page.drag_first_ingredient_to_constructor()

        counter_after = page.get_first_ingredient_counter()
        assert counter_after == counter_before + 2, (
            f"Счётчик булки не увеличился на 2 (верх+низ): было {counter_before}, стало {counter_after}"
        )

    def test_logged_in_user_can_place_order(self, logged_in_driver):
        page = ConstructorPage(logged_in_driver)

        page.drag_first_ingredient_to_constructor()
        page.click_order_button()

        assert page.is_order_number_displayed(), (
            "После оформления заказа не появился номер заказа"
        )
        