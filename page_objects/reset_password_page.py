from locators.reset_password_locators import ResetPasswordLocators
from page_objects.main_page import MainPage
import allure


class ResetPasswordPage(MainPage):
    @allure.step("Ожидание появления элемента 'Введите код из письма'")
    def wait_for_code_label(self):
        self.wait_for_element(ResetPasswordLocators.CODE_INPUT_LABEL)

    @allure.step("Проверка отображения элемента 'Введите код из письма'")
    def is_code_label_displayed(self):
        return self.is_element_visible(ResetPasswordLocators.CODE_INPUT_LABEL)

    @allure.step("Ожидание появления поля для ввода пароля")
    def wait_for_password_input(self):
        self.wait_for_element_to_be_visible(ResetPasswordLocators.PASSWORD_INPUT)

    @allure.step("Ввод нового пароля в поле")
    def enter_password(self, password):
        password_input = self.find_element(ResetPasswordLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

    @allure.step('Проверка, что тип поля для пароля — "password"')
    def is_password_input_type_password(self):
        password_input = self.find_element(ResetPasswordLocators.PASSWORD_INPUT)
        return password_input.get_attribute("type") == "password"

    @allure.step('Проверка, что тип поля для пароля — "text"')
    def is_password_input_type_text(self):
        password_input = self.find_element(ResetPasswordLocators.PASSWORD_INPUT)
        return password_input.get_attribute("type") == "text"

    @allure.step('Клик на иконку "Показать/Скрыть пароль"')
    def click_show_password_button(self):
        show_password_button = self.find_element(ResetPasswordLocators.SHOW_PASSWORD_BUTTON)
        show_password_button.click()
