import allure

from constants import BASE_URL
from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators as Locators


DRAG_AND_DROP_JS = """
function fireEvent(element, type, dataTransfer, clientX, clientY) {
    const event = new Event(type, { bubbles: true, cancelable: true });
    event.dataTransfer = dataTransfer;
    event.clientX = clientX;
    event.clientY = clientY;
    element.dispatchEvent(event);
}

const source = arguments[0];
const target = arguments[1];
const dataTransfer = new DataTransfer();

const sourceRect = source.getBoundingClientRect();
const targetRect = target.getBoundingClientRect();

const startX = sourceRect.left + sourceRect.width / 2;
const startY = sourceRect.top + sourceRect.height / 2;
const endX = targetRect.left + targetRect.width / 2;
const endY = targetRect.top + targetRect.height / 2;

fireEvent(source, 'dragstart', dataTransfer, startX, startY);
fireEvent(target, 'dragenter', dataTransfer, endX, endY);
fireEvent(target, 'dragover', dataTransfer, endX, endY);
fireEvent(target, 'drop', dataTransfer, endX, endY);
fireEvent(source, 'dragend', dataTransfer, endX, endY);
"""


class ConstructorPage(BasePage):

    @allure.step("Открыть страницу конструктора")
    def open_constructor_page(self):
        self.driver.get(BASE_URL)

    @allure.step("Кликнуть по ссылке 'Конструктор' в шапке")
    def click_constructor_link(self):
        self.click(Locators.CONSTRUCTOR_LINK)

    @allure.step("Кликнуть по ссылке 'Лента Заказов' в шапке")
    def click_feed_link(self):
        self.click(Locators.FEED_LINK)

    @allure.step("Кликнуть по первому ингредиенту в списке")
    def click_first_ingredient(self):
        self.click(Locators.FIRST_INGREDIENT_CARD)

    @allure.step("Проверить, что открыто окно с деталями ингредиента")
    def is_ingredient_modal_opened(self):
        return self.is_element_visible(Locators.MODAL_INGREDIENT_TITLE)

    @allure.step("Закрыть модальное окно по крестику")
    def close_modal(self):
        self.click(Locators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модальное окно закрылось")
    def is_modal_closed(self):
        try:
            self.wait.until_not(
                lambda driver: driver.find_element(*Locators.MODAL_CONTAINER).is_displayed()
            )
            return True
        except Exception:
            return False

    @allure.step("Получить значение счётчика первого ингредиента")
    def get_first_ingredient_counter(self):
        card = self.find_element(Locators.FIRST_INGREDIENT_CARD)
        try:
            counter = card.find_element(*Locators.INGREDIENT_COUNTER)
            return int(counter.text)
        except Exception:
            return 0

    @allure.step("Перетащить первый ингредиент в зону сборки бургера")
    def drag_first_ingredient_to_constructor(self):
        source = self.find_element(Locators.FIRST_INGREDIENT_CARD)
        target = self.find_element(Locators.BUN_DROP_ZONE)
        self.driver.execute_script(DRAG_AND_DROP_JS, source, target)

    @allure.step("Кликнуть по кнопке 'Оформить заказ'")
    def click_order_button(self):
        self.click(Locators.ORDER_BUTTON)

    @allure.step("Проверить, что отобразился номер заказа")
    def is_order_number_displayed(self):
        return self.is_element_visible(Locators.ORDER_NUMBER, timeout=15)

    @allure.step("Получить текст номера оформленного заказа")
    def get_order_number_text(self):
        element = self.find_element(Locators.ORDER_NUMBER)
        return element.text
    