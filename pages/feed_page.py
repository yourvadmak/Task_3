from pages.base_page import BasePage
from locators.feed_locators import FeedLocators as Locators


class FeedPage(BasePage):
    def click_first_order(self):
        self.click(Locators.FIRST_ORDER_CARD)

    def is_order_modal_opened(self):
        return self.is_element_visible(Locators.MODAL_CONTAINER, timeout=15)

    def get_total_completed_count(self):
        element = self.find_element(Locators.TOTAL_COMPLETED_COUNT)
        return int(element.text)

    def get_today_completed_count(self):
        element = self.find_element(Locators.TODAY_COMPLETED_COUNT)
        return int(element.text)

    def is_order_number_in_progress_or_ready(self, order_number):
        in_progress_list = self.find_element(Locators.IN_PROGRESS_ORDERS_LIST)
        ready_list = self.find_element(Locators.READY_ORDERS_LIST)
        return order_number in in_progress_list.text or order_number in ready_list.text

    def get_order_history_numbers(self):
        cards = self.driver.find_elements(*Locators.ORDER_HISTORY_LIST)
        return [card.text for card in cards]
    