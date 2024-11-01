from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient') and contains(@href, '/ingredient/') "
                            "and .//p[text()='Мясо бессмертных моллюсков Protostomia']]")

    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__container') "
                              "and .//h2[text()='Детали ингредиента']]")

    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//button[contains(@class, "
                                    "'Modal_modal__close')]")

    MODAL_INGREDIENT_NAME = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//p[contains(@class, "
                                       "'text_type_main-medium') and text()='Мясо бессмертных моллюсков Protostomia']")

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and text()='Конструктор']")

    INGREDIENT_COUNTER = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') "
                                    "and @href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[contains(@class, "
                                    "'counter_counter__num__3nue1')]")

    FLUORESCENT_BUN_LINK = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') "
                                      "and @href='/ingredient/61c0c5a71d1f82001bdaaa6d']")

    UPPER_BUN = (By.XPATH, "//div[@class='constructor-element "
                           "constructor-element_pos_top']//span[@class='constructor-element__text']")

    LOWER_BUN = (By.XPATH, "//div[@class='constructor-element "
                           "constructor-element_pos_bottom']//span[@class='constructor-element__text']")

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') "
                                    "and contains(@class, 'button_button_type_primary__1O7Bx') "
                                    "and contains(@class, 'button_button_size_large__G21Vg') "
                                    "and text()='Оформить заказ']")

    ORDER_CONFIRMATION = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")

    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m') and contains(@class, "
                              "'text_type_digits-large')]")

    DEFAULT_ORDER_NUMBER_9999 = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') "
                              "and contains(@class, 'Modal_modal__title__2L34m') "
                              "and contains(@class, 'text_type_digits-large') and text() = '9999']")
