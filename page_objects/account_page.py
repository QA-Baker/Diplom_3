from locators.account_page_locators import AccountPageLocators
from page_objects.base_page import BasePage
import allure


class AccountPage(BasePage):

    @allure.step("Переход в Личный кабинет")
    def go_to_account(self):
        self.click_element_with_js(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step("Переход в раздел 'История заказов'")
    def go_to_order_history(self):
        self.click_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Выход из аккаунта")
    def click_logout_button(self):
        self.click_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step("Ожидание появления кнопки Оформить заказ")
    def wait_for_order_button(self):
        self.wait_for_element(AccountPageLocators.ORDER_BUTTON)

    @allure.step("Ожидание URL личного кабинета")
    def wait_for_account_url(self):
        self.wait_for_url_contains("account/profile")

    @allure.step("Ожидание URL истории заказов личного кабинета")
    def wait_for_account_history_url(self):
        self.wait_for_url_contains("account/order-history")
