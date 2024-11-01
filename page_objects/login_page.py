from locators.login_page_locators import LoginPageLocators
from page_objects.main_page import MainPage
import allure


class LoginPage(MainPage):

    @allure.step("Клик на ссылку 'Восстановить пароль'")
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Использование клика с помощью JavaScript")
    def click_forgot_password_link(self):
        self.click_element_with_js(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Ввести email и пароль")
    def enter_credentials(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажать на кнопку 'Войти'")
    def click_login_button(self):
        self.click_element_with_js(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Ожидание кнопки 'Войти'")
    def wait_for_login_button(self):
        self.wait_for_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Логин")
    def login(self, email, password):
        self.go_to_login_page()
        self.enter_credentials(email, password)
        self.click_login_button()
