import allure
from data import USER_EMAIL, USER_PASSWORD
from locators.constructor_page_locators import ConstructorPageLocators
from page_objects.account_page import AccountPage
from page_objects.constructor_page import ConstructorPage
from page_objects.login_page import LoginPage
from page_objects.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Открытие всплывающего окна с деталями заказа по клику")
    def test_order_details_modal_display(self, driver):
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        account_page = AccountPage(driver)
        with allure.step("Авторизация"):
            login_page.login(USER_EMAIL, USER_PASSWORD)
            account_page.wait_for_order_button()
        with allure.step("Переход на страницу ленты заказов"):
            order_feed_page.go_to_feed_page()
        with allure.step("Клик по заказу в ленте"):
            order_feed_page.click_on_order()
        with allure.step("Проверка, что модальное окно с деталями заказа отображается"):
            assert order_feed_page.is_order_modal_displayed(), \
                "Всплывающее окно не появилось"

    @allure.title("Заказы пользователя отображаются в 'Истории заказов'")
    def test_user_orders_in_history(self, driver):
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        account_page = AccountPage(driver)
        constructor_page = ConstructorPage(driver)
        with allure.step("Авторизация"):
            login_page.login(USER_EMAIL, USER_PASSWORD)
            account_page.wait_for_order_button()
        with allure.step("Локатор конкретного ингредиента и области конструктора"):
            specific_ingredient = constructor_page.get_element(ConstructorPageLocators.FLUORESCENT_BUN_LINK)
            constructor_area = constructor_page.get_element(ConstructorPageLocators.UPPER_BUN)
        with allure.step("Перетаскивание ингредиента в область конструктора"):
            constructor_page.drag_and_drop_ingredient(specific_ingredient, constructor_area)
        with allure.step("Локатор второго ингредиента и области конструктора"):
            specific_ingredient = constructor_page.get_element(ConstructorPageLocators.INGREDIENT)
            constructor_area = constructor_page.get_element(ConstructorPageLocators.LOWER_BUN)
        with allure.step("Перетаскивание второго ингредиента в область конструктора"):
            constructor_page.drag_and_drop_ingredient(specific_ingredient, constructor_area)
        with allure.step("Клик по кнопке 'Оформить заказ'"):
            constructor_page.click_place_order_button()
        with allure.step("Проверка успешного оформления заказа"):
            assert constructor_page.is_order_successful(), "Не удалось оформить заказ для залогиненного пользователя"
        with allure.step("Ожидание исчезновения дефолтного номера заказа '9999'"):
            constructor_page.wait_for_element_invisibility(ConstructorPageLocators.DEFAULT_ORDER_NUMBER_9999)
        with allure.step("Извлечение номера заказа"):
            order_number_element = constructor_page.get_element(ConstructorPageLocators.ORDER_NUMBER)
            order_number = int(order_number_element.text.strip())
        with allure.step("Закрытие окна с номером заказа"):
            order_feed_page.close_modal()
        with allure.step("Переход в личный кабинет"):
            account_page.go_to_account()
        with allure.step("Переход в раздел 'История заказов'"):
            account_page.go_to_order_history()
        with allure.step("Добавление ведущего нуля к номеру заказа для проверки"):
            formatted_order_number = str(order_number).zfill(7)
        with allure.step("Проверка, что заказ с нужным номером отображается в истории заказов"):
            assert order_feed_page.is_order_number_in_history(formatted_order_number), \
                f"Order number {formatted_order_number} not found in order history."
        with allure.step("Переход в ленту заказов"):
            order_feed_page.go_to_feed_page()
        with allure.step("Проверка, что заказ с нужным номером отображается в ленте заказов"):
            assert order_feed_page.is_order_number_in_history(formatted_order_number), \
                f"Order number {formatted_order_number} not found in feed."

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается при создании нового заказа")
    def test_total_completed_orders_counter_increases(self, driver):
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        account_page = AccountPage(driver)
        constructor_page = ConstructorPage(driver)
        with allure.step("Авторизация"):
            login_page.login(USER_EMAIL, USER_PASSWORD)
            account_page.wait_for_order_button()
        with allure.step("Переход на страницу ленты заказов"):
            order_feed_page.go_to_feed_page()
        with allure.step("Получение значения счётчика 'Выполнено за всё время'"):
            initial_completed_orders = int(order_feed_page.get_total_completed_orders_count())
        with allure.step("Переход на страницу конструктора"):
            order_feed_page.click_constructor_button()
        with allure.step("Локатор конкретного ингредиента и области конструктора"):
            specific_ingredient = constructor_page.get_element(ConstructorPageLocators.FLUORESCENT_BUN_LINK)
            constructor_area = constructor_page.get_element(ConstructorPageLocators.UPPER_BUN)
        with allure.step("Перетаскивание ингредиента в область конструктора"):
            constructor_page.drag_and_drop_ingredient(specific_ingredient, constructor_area)
        with allure.step("Локатор второго ингредиента и области конструктора"):
            specific_ingredient = constructor_page.get_element(ConstructorPageLocators.INGREDIENT)
            constructor_area = constructor_page.get_element(ConstructorPageLocators.LOWER_BUN)
        with allure.step("Перетаскивание второго ингредиента в область конструктора"):
            constructor_page.drag_and_drop_ingredient(specific_ingredient, constructor_area)
        with allure.step("Клик по кнопке 'Оформить заказ'"):
            constructor_page.click_place_order_button()
        with allure.step("Проверка успешного оформления заказа"):
            assert constructor_page.is_order_successful(), "Не удалось оформить заказ для залогиненного пользователя"
        with allure.step("Закрытие окна с номером заказа"):
            order_feed_page.close_modal()
        with allure.step("Переход на страницу ленты заказов"):
            order_feed_page.go_to_feed_page()
        with allure.step("Получение нового значения счётчика 'Выполнено за всё время'"):
            updated_completed_orders = int(order_feed_page.get_total_completed_orders_count())
        with allure.step("Проверка, что значение счётчика увеличилось"):
            assert updated_completed_orders > initial_completed_orders, \
                "Счётчик 'Выполнено за всё время' не увеличился после создания нового заказа"

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается при создании нового заказа")
    def test_daily_completed_orders_counter_increases(self, driver):
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        account_page = AccountPage(driver)
        constructor_page = ConstructorPage(driver)
        with allure.step("Авторизация"):
            login_page.login(USER_EMAIL, USER_PASSWORD)
            account_page.wait_for_order_button()
        with allure.step("Переход на страницу ленты заказов"):
            order_feed_page.go_to_feed_page()
        with allure.step("Получение значения счётчика 'Выполнено за сегодня'"):
            initial_daily_completed_orders = int(order_feed_page.get_daily_completed_orders_count())
        with allure.step("Переход на страницу конструктора"):
            order_feed_page.click_constructor_button()
        with allure.step("Перетаскивание первого ингредиента"):
            specific_ingredient = constructor_page.get_element(ConstructorPageLocators.FLUORESCENT_BUN_LINK)
            constructor_area = constructor_page.get_element(ConstructorPageLocators.UPPER_BUN)
            constructor_page.drag_and_drop_ingredient(specific_ingredient, constructor_area)
        with allure.step("Перетаскивание второго ингредиента"):
            specific_ingredient = constructor_page.get_element(ConstructorPageLocators.INGREDIENT)
            constructor_area = constructor_page.get_element(ConstructorPageLocators.LOWER_BUN)
            constructor_page.drag_and_drop_ingredient(specific_ingredient, constructor_area)
        with allure.step("Клик по кнопке 'Оформить заказ'"):
            constructor_page.click_place_order_button()
        with allure.step("Проверка успешного оформления заказа"):
            assert constructor_page.is_order_successful(), "Не удалось оформить заказ для залогиненного пользователя"
        with allure.step("Закрытие окна с номером заказа"):
            order_feed_page.close_modal()
        with allure.step("Переход на страницу ленты заказов"):
            order_feed_page.go_to_feed_page()
        with allure.step("Получение нового значения счётчика 'Выполнено за сегодня'"):
            updated_daily_completed_orders = int(order_feed_page.get_daily_completed_orders_count())
        with allure.step("Проверка, что значение счётчика увеличилось"):
            assert updated_daily_completed_orders > initial_daily_completed_orders, \
                "Счётчик 'Выполнено за сегодня' не увеличился после создания нового заказа"

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_appears_in_progress_section(self, driver):
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        account_page = AccountPage(driver)
        constructor_page = ConstructorPage(driver)
        with allure.step("Авторизация"):
            login_page.login(USER_EMAIL, USER_PASSWORD)
            account_page.wait_for_order_button()
        with allure.step("Перетаскивание первого ингредиента"):
            specific_ingredient = constructor_page.get_element(ConstructorPageLocators.FLUORESCENT_BUN_LINK)
            constructor_area = constructor_page.get_element(ConstructorPageLocators.UPPER_BUN)
            constructor_page.drag_and_drop_ingredient(specific_ingredient, constructor_area)
        with allure.step("Перетаскивание второго ингредиента"):
            specific_ingredient = constructor_page.get_element(ConstructorPageLocators.INGREDIENT)
            constructor_area = constructor_page.get_element(ConstructorPageLocators.LOWER_BUN)
            constructor_page.drag_and_drop_ingredient(specific_ingredient, constructor_area)
        with allure.step("Клик по кнопке 'Оформить заказ'"):
            constructor_page.click_place_order_button()
        with allure.step("Проверка успешного оформления заказа"):
            assert constructor_page.is_order_successful(), "Не удалось оформить заказ для залогиненного пользователя"
        with allure.step("Ожидание, что дефолтный номер заказа '9999' станет невидимым"):
            constructor_page.wait_for_element_invisibility(ConstructorPageLocators.DEFAULT_ORDER_NUMBER_9999)
        with allure.step("Извлечение номера заказа"):
            order_number_element = constructor_page.get_element(ConstructorPageLocators.ORDER_NUMBER)
            order_number = int(order_number_element.text.strip())
        with allure.step("Закрытие окна с номером заказа"):
            order_feed_page.close_modal()
        with allure.step("Переход на страницу ленты заказов"):
            order_feed_page.go_to_feed_page()
        with allure.step("Ожидание появления заказа в разделе 'В работе'"):
            order_feed_page.wait_for_order_number_in_progress(order_number)
        with allure.step("Проверка, что номер нового заказа присутствует в разделе 'В работе'"):
            order_numbers_in_progress = order_feed_page.get_in_progress_order_numbers()
            assert order_number in order_numbers_in_progress, (f"Номер заказа {order_number} "
                                                               f"не найден в разделе 'В работе'")
