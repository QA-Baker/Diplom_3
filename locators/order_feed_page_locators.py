from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and text()='Лента Заказов']")

    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "p.AppHeader_header__linkText__3q_va.ml-2")

    FIRST_ORDER_ITEM = (By.XPATH, "//main/div/div/ul/li[1]")

    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[@type='button' "
                                    "and contains(@class, 'Modal_modal__close')]")

    TOTAL_ORDERS_COMPLETED = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, "
                                        "'OrderFeed_number__2MbrQ') and contains(@class, 'text_type_digits-large')]")

    DAILY_ORDERS_COMPLETED = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, "
                                        "'OrderFeed_number__2MbrQ') and contains(@class, 'text_type_digits-large')]")

    IN_PROGRESS_ORDERS = (By.CSS_SELECTOR, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem') "
                                           "and contains(@class, 'OrderFeed_orderList__cBvyi')]//li[contains(@class, "
                                           "'text_type_digits-default') and contains(@class, 'mb-2')]")

    IN_PROGRESS_SECTION = (By.CLASS_NAME, "OrderFeed_orderListReady__1YFem")

    IN_PROGRESS_ORDER_NUMBER = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem .text_type_digits-default.mb-2")

    ORDER_HISTORY_NUMBER = (By.CSS_SELECTOR, "p.text.text_type_digits-default")
