import time

from constants import BASE_URL
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.personal_account_page import PersonalAccountPage
from locators.constructor_locators import ConstructorLocators
from locators.feed_locators import FeedLocators


class TestOrderFeed:
    def test_click_order_opens_modal(self, driver):
        driver.get(f"{BASE_URL}/feed")
        page = FeedPage(driver)
        page.wait_for_elements_present(FeedLocators.ORDER_CARDS_LIST)

        page.click_first_order()

        assert page.is_order_modal_opened(), (
            "Клик по заказу не открыл окно с деталями"
        )

    def test_order_history_matches_feed(self, logged_in_driver):
        constructor_page = ConstructorPage(logged_in_driver)
        constructor_page.drag_first_ingredient_to_constructor()
        constructor_page.click_order_button()
        constructor_page.wait_for_text_not_equal(ConstructorLocators.ORDER_NUMBER, "9999", timeout=15)

        account_page = PersonalAccountPage(logged_in_driver)
        account_page.click_personal_account_link()
        account_page.click_order_history_tab()

        feed_page = FeedPage(logged_in_driver)
        feed_page.wait_for_elements_present(FeedLocators.ORDER_HISTORY_LIST)
        history_numbers = feed_page.get_order_history_numbers()

        assert len(history_numbers) > 0, (
            "В истории заказов нет заказов после оформления"
        )

    def test_new_order_increases_total_count(self, logged_in_driver):
        logged_in_driver.get(f"{BASE_URL}/feed")
        feed_page = FeedPage(logged_in_driver)
        count_before = feed_page.get_total_completed_count()

        constructor_page = ConstructorPage(logged_in_driver)
        constructor_page.click_constructor_link()
        constructor_page.drag_first_ingredient_to_constructor()
        constructor_page.click_order_button()
        constructor_page.wait_for_text_not_equal(ConstructorLocators.ORDER_NUMBER, "9999", timeout=15)

        logged_in_driver.get(f"{BASE_URL}/feed")
        time.sleep(2)
        count_after = feed_page.get_total_completed_count()

        assert count_after >= count_before, (
            f"Счётчик 'Выполнено за всё время' не увеличился: было {count_before}, стало {count_after}"
        )

    def test_new_order_increases_today_count(self, logged_in_driver):
        logged_in_driver.get(f"{BASE_URL}/feed")
        feed_page = FeedPage(logged_in_driver)
        count_before = feed_page.get_today_completed_count()

        constructor_page = ConstructorPage(logged_in_driver)
        constructor_page.click_constructor_link()
        constructor_page.drag_first_ingredient_to_constructor()
        constructor_page.click_order_button()
        constructor_page.wait_for_text_not_equal(ConstructorLocators.ORDER_NUMBER, "9999", timeout=15)

        logged_in_driver.get(f"{BASE_URL}/feed")
        time.sleep(2)
        count_after = feed_page.get_today_completed_count()

        assert count_after >= count_before, (
            f"Счётчик 'Выполнено за сегодня' не увеличился: было {count_before}, стало {count_after}"
        )

    def test_new_order_appears_in_progress_list(self, logged_in_driver):
        constructor_page = ConstructorPage(logged_in_driver)
        constructor_page.drag_first_ingredient_to_constructor()
        constructor_page.click_order_button()
        constructor_page.wait_for_text_not_equal(ConstructorLocators.ORDER_NUMBER, "9999", timeout=15)

        order_number_element = logged_in_driver.find_element(*ConstructorLocators.ORDER_NUMBER)
        order_number = order_number_element.text

        logged_in_driver.get(f"{BASE_URL}/feed")
        feed_page = FeedPage(logged_in_driver)

        assert feed_page.is_order_number_in_progress_or_ready(order_number), (
            f"Номер заказа {order_number} не найден ни в 'В работе', ни в 'Готовы'"
        )
