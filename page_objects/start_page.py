from locators.order_feed_page_locators import FeedPageLocators
from page_objects.base_page import BasePage
import allure


@allure.step("Клик по кнопке 'Лента заказов'")
class StartPage(BasePage):
    def click_order_feed_button(self):
        self.wait_for_element_to_be_clickable(FeedPageLocators.ORDER_FEED_BUTTON).click()
