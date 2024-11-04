import allure
from data import BASE_URL, ORDER_FEED_URL, USER_EMAIL, USER_PASSWORD
from page_objects.constructor_page import ConstructorPage
from page_objects.order_feed_page import OrderFeedPage
from page_objects.login_page import LoginPage
from locators.constructor_page_locators import ConstructorPageLocators
from page_objects.start_page import StartPage


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_navigate_to_constructor(self, driver):
        order_feed_page = OrderFeedPage(driver)
        with allure.step("Переход на страницу ленты заказов"):
            order_feed_page.go_to_feed_page()
        with allure.step("Клик по кнопке 'Конструктор'"):
            order_feed_page.click_constructor_button()
        with allure.step("Проверка перехода на страницу конструктора"):
            expected_url = BASE_URL.rstrip('/')
            actual_url = driver.current_url.rstrip('/')
            assert actual_url == expected_url, \
                f"Не удалось перейти на страницу конструктора. Ожидался URL: {expected_url}, получен: {actual_url}"

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigate_to_order_feed(self, driver):
        start_page = StartPage(driver)
        with allure.step("Открытие главной страницы"):
            start_page.go_to_main_page()
        with allure.step("Клик по кнопке 'Лента заказов'"):
            start_page.click_order_feed_button()
        with allure.step("Проверка перехода на страницу 'Лента заказов'"):
            expected_url = ORDER_FEED_URL.rstrip('/')
            actual_url = driver.current_url.rstrip('/')
            assert actual_url == expected_url, \
                f"Не удалось перейти на страницу Ленты заказов. Ожидался URL: {expected_url}, получен: {actual_url}"

    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    def test_ingredient_modal_display(self, driver):
        constructor_page = ConstructorPage(driver)
        with allure.step("Переход на страницу конструктора"):
            constructor_page.go_to_main_page()
            assert constructor_page.is_on_constructor_page(), "Не удалось открыть страницу конструктора"
        specific_ingredient_locator = ConstructorPageLocators.INGREDIENT
        with allure.step("Клик по ингредиенту"):
            constructor_page.click_ingredient(specific_ingredient_locator)
        with allure.step("Проверка отображения модального окна"):
            assert constructor_page.is_modal_displayed(), "Всплывающее окно с деталями ингредиента не появилось"
        with allure.step("Проверка наличия названия ингредиента в модальном окне"):
            ingredient_name = constructor_page.get_modal_ingredient_name()
            assert ingredient_name, "Название ингредиента в модальном окне отсутствует"

    @allure.title("Закрытие всплывающего окна по клику на крестик")
    def test_close_modal_by_clicking_cross(self, driver):
        constructor_page = ConstructorPage(driver)
        with allure.step("Переход на страницу конструктора"):
            constructor_page.go_to_main_page()
            assert constructor_page.is_on_constructor_page(), "Не удалось открыть страницу конструктора"
        specific_ingredient_locator = ConstructorPageLocators.INGREDIENT
        with allure.step("Клик по ингредиенту"):
            constructor_page.click_ingredient(specific_ingredient_locator)
            assert constructor_page.is_modal_displayed(), "Всплывающее окно с деталями ингредиента не появилось"
        with allure.step("Закрытие модального окна по клику на крестик"):
            constructor_page.close_modal()
            constructor_page.wait_for_element_to_be_invisible(ConstructorPageLocators.MODAL_WINDOW)
            assert not constructor_page.is_modal_displayed(), "Всплывающее окно с деталями ингредиента не закрыто"

    @allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increases(self, driver):
        constructor_page = ConstructorPage(driver)
        with allure.step("Переход на страницу конструктора"):
            constructor_page.go_to_main_page()
            assert constructor_page.is_on_constructor_page(), "Не удалось открыть страницу конструктора"
        specific_ingredient = constructor_page.get_element(ConstructorPageLocators.FLUORESCENT_BUN_LINK)
        constructor_area = constructor_page.get_element(ConstructorPageLocators.UPPER_BUN)
        with allure.step("Получение начального значения счётчика ингредиента"):
            initial_count = constructor_page.get_ingredient_counter(ConstructorPageLocators.INGREDIENT_COUNTER)
        with allure.step("Перетаскивание ингредиента в область конструктора"):
            constructor_page.drag_and_drop_ingredient(specific_ingredient, constructor_area)
        with allure.step("Проверка увеличения счётчика ингредиента"):
            new_count = constructor_page.get_ingredient_counter(ConstructorPageLocators.INGREDIENT_COUNTER)
            assert new_count > initial_count, "Счётчик ингредиента не увеличился при добавлении в заказ"

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_place_order(self, driver):
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        with allure.step("Авторизация пользователя"):
            login_page.login(USER_EMAIL, USER_PASSWORD)
        with allure.step("Переход на страницу конструктора"):
            constructor_page.go_to_constructor_page()
        specific_ingredient = constructor_page.get_element(ConstructorPageLocators.INGREDIENT)
        constructor_area = constructor_page.get_element(ConstructorPageLocators.LOWER_BUN)
        with allure.step("Перетаскивание ингредиента в область конструктора"):
            constructor_page.drag_and_drop_ingredient(specific_ingredient, constructor_area)
        with allure.step("Клик по кнопке 'Оформить заказ'"):
            constructor_page.click_place_order_button()
        with allure.step("Проверка успешного оформления заказа"):
            assert constructor_page.is_order_successful(), "Не удалось оформить заказ для залогиненного пользователя"
