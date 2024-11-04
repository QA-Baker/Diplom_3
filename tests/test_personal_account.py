import allure
from data import USER_EMAIL, USER_PASSWORD, ACCOUNT_URL, ORDER_HISTORY_URL
from locators.login_page_locators import LoginPageLocators
from page_objects.login_page import LoginPage
from page_objects.account_page import AccountPage


@allure.feature("Личный кабинет")
class TestAccount:

    @allure.title("Переход по клику на 'Личный кабинет'")
    def test_navigate_to_account(self, driver):
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        with allure.step("Авторизация пользователя"):
            login_page.login(USER_EMAIL, USER_PASSWORD)
            account_page.wait_for_order_button()
        with allure.step("Переход в личный кабинет"):
            account_page.go_to_account()
        with allure.step("Проверка перехода на страницу личного кабинета"):
            account_page.wait_for_account_url()
            expected_url = ACCOUNT_URL
            actual_url = driver.current_url
            assert actual_url == expected_url, \
                f"Не удалось перейти на страницу Личного кабинета. Ожидался URL: {expected_url}, получен: {actual_url}"

    @allure.title("Переход в раздел 'История заказов'")
    def test_navigate_to_order_history(self, driver):
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        with allure.step("Авторизация пользователя"):
            login_page.login(USER_EMAIL, USER_PASSWORD)
            account_page.wait_for_order_button()
        with allure.step("Переход в личный кабинет"):
            account_page.go_to_account()
        with allure.step("Переход в раздел 'История заказов'"):
            account_page.go_to_order_history()
        with allure.step("Проверка открытия страницы с историей заказов"):
            account_page.wait_for_account_history_url()
            expected_url = ORDER_HISTORY_URL
            actual_url = driver.current_url
            assert actual_url == expected_url, \
                f"Не удалось перейти на страницу Истории заказов. Ожидался URL: {expected_url}, получен: {actual_url}"

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        with allure.step("Авторизация пользователя"):
            login_page.login(USER_EMAIL, USER_PASSWORD)
            account_page.wait_for_order_button()
        with allure.step("Переход в личный кабинет"):
            account_page.go_to_account()
        with allure.step("Выход из аккаунта"):
            account_page.click_logout_button()
        with allure.step("Ожидание появления кнопки 'Войти' после выхода"):
            login_page.wait_for_login_button()
        with allure.step("Проверка отображения кнопки 'Войти' на странице логина"):
            assert login_page.is_element_visible(LoginPageLocators.LOGIN_BUTTON), \
                "Кнопка 'Войти' не отображается после выхода из аккаунта"
