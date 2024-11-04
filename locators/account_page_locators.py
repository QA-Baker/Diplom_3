from selenium.webdriver.common.by import By


class AccountPageLocators:
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, "История заказов")

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    ACCOUNT_BUTTON = (By.XPATH,
                      "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']")

    ORDER_BUTTON = (By.XPATH,
                    "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Оформить заказ')]")
