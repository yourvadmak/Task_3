from selenium.webdriver.common.by import By


class FeedLocators:
    ORDER_CARDS_LIST = (By.XPATH, "//a[contains(@class, 'OrderHistory_link__')]")
    FIRST_ORDER_CARD = (By.XPATH, "(//a[contains(@class, 'OrderHistory_link__')])[1]")
    MODAL_CONTAINER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//div[contains(@class, 'Modal_modal__container')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")

    TOTAL_COMPLETED_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COMPLETED_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    READY_ORDERS_LIST = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_orderList__')])[1]")
    IN_PROGRESS_ORDERS_LIST = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_orderList__')])[2]")

    ORDER_HISTORY_LIST = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")
    