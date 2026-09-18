from selenium.webdriver.common.by import By


class ConstructorLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']")

    FIRST_INGREDIENT_CARD = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__')])[1]")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter_counter__num__3nue1")

    BUN_DROP_ZONE = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")

    MODAL_CONTAINER = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close__TnseK")
    MODAL_INGREDIENT_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    ORDER_NUMBER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")

    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    