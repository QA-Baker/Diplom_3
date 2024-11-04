import data
from locators.forgot_password_locators import ForgotPasswordLocators
from page_objects.base_page import BasePage
import allure


class ForgotPasswordPage(BasePage):

    @allure.step("Открытие страницы восстановления пароля")
    def go_to_forgot_password_page(self):
        self.driver.get(data.FORGOT_PASSWORD_URL)

    @allure.step("Ввод email")
    def enter_email(self, email):
        self.wait_for_element(ForgotPasswordLocators.EMAIL_INPUT).send_keys(email)

    @allure.step("Клик на кнопку 'Восстановить'")
    def click_restore_button(self):
        self.click_element_with_js(ForgotPasswordLocators.RESTORE_BUTTON)
