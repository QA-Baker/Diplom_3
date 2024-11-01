import allure
from page_objects.login_page import LoginPage
from page_objects.forgot_password_page import ForgotPasswordPage
from page_objects.reset_password_page import ResetPasswordPage


@allure.feature("Восстановление пароля")
class TestForgotPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_navigate_to_forgot_password(self, driver):
        login_page = LoginPage(driver)
        with allure.step("Переход на страницу логина"):
            login_page.go_to_login_page()
        with allure.step("Клик по ссылке 'Восстановить пароль'"):
            login_page.click_forgot_password_link()
        with allure.step("Проверка перехода на страницу восстановления пароля"):
            assert "forgot-password" in driver.current_url, "Не удалось перейти на страницу восстановления пароля"

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_enter_email_and_click_restore(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        with allure.step("Открытие страницы восстановления пароля"):
            forgot_password_page.go_to_forgot_password_page()
        with allure.step("Ввод email и клик на кнопку 'Восстановить'"):
            forgot_password_page.enter_email("popov_13@gmail.com")
            forgot_password_page.click_restore_button()
        with allure.step("Ожидание элемента 'Введите код из письма'"):
            reset_password_page.wait_for_code_label()
        with allure.step("Проверка, что элемент с текстом 'Введите код из письма' отображается на странице"):
            assert reset_password_page.is_code_label_displayed(), "Элемент 'Введите код из письма' не отображается"

    @allure.title("Проверка работы кнопки 'Показать/Скрыть пароль'")
    def test_show_hide_password(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        with allure.step("Открытие страницы восстановления пароля"):
            forgot_password_page.go_to_forgot_password_page()
        with allure.step("Ввод email и клик на кнопку 'Восстановить'"):
            forgot_password_page.enter_email("popov_13@gmail.com")
            forgot_password_page.click_restore_button()
        with allure.step("Ожидание появления поля для ввода пароля"):
            reset_password_page.wait_for_password_input()
        with allure.step("Ввод нового пароля"):
            reset_password_page.enter_password("Stellarburgers1234!")
        with allure.step("Проверка, что тип поля для пароля — 'password'"):
            assert reset_password_page.is_password_input_type_password(), \
                "Поле пароля должно быть скрытым (type='password')"
        with allure.step("Клик на кнопку 'Показать/Скрыть пароль'"):
            reset_password_page.click_show_password_button()
        with allure.step("Проверка, что тип поля для пароля изменился на 'text'"):
            assert reset_password_page.is_password_input_type_text(), "Поле пароля должно отображаться (type='text')"
