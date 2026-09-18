import allure
from selenium.webdriver.support.ui import WebDriverWait

from constants import BASE_URL
from pages.base_page import BasePage
from locators.feed_locators import FeedLocators as Locators


class FeedPage(BasePage):

    @allure.step("Открыть страницу 'Лента заказов'")
    def open_feed_page(self):
        self.driver.get(f"{BASE_URL}/feed")

    @allure.step("Кликнуть по первому заказу в ленте")
    def click_first_order(self):
        self.click(Locators.FIRST_ORDER_CARD)

    @allure.step("Проверить, что открыто модальное окно заказа")
    def is_order_modal_opened(self):
        return self.is_element_visible(Locators.MODAL_CONTAINER, timeout=15)

    @allure.step("Получить счётчик 'Выполнено за всё время'")
    def get_total_completed_count(self):
        element = self.find_element(Locators.TOTAL_COMPLETED_COUNT)
        return int(element.text)

    @allure.step("Получить счётчик 'Выполнено за сегодня'")
    def get_today_completed_count(self):
        element = self.find_element(Locators.TODAY_COMPLETED_COUNT)
        return int(element.text)

    @allure.step("Проверить наличие номера заказа в разделах 'В работе'/'Готовы'")
    def is_order_number_in_progress_or_ready(self, order_number):
        in_progress_list = self.find_element(Locators.IN_PROGRESS_ORDERS_LIST)
        ready_list = self.find_element(Locators.READY_ORDERS_LIST)
        return order_number in in_progress_list.text or order_number in ready_list.text

    @allure.step("Дождаться появления заказа в разделах 'В работе' или 'Готовы'")
    def wait_for_order_in_progress_or_ready(self, order_number, timeout=30):
        wait = WebDriverWait(self.driver, timeout, poll_frequency=2)

        def check(driver):
            self.open_feed_page()
            return self.is_order_number_in_progress_or_ready(order_number)

        wait.until(check)

    @allure.step("Получить номера заказов из истории")
    def get_order_history_numbers(self):
        cards = self.driver.find_elements(*Locators.ORDER_HISTORY_LIST)
        return [card.text for card in cards]
    