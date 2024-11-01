from selenium.common import TimeoutException
from data import ORDER_FEED_URL
from locators.order_feed_page_locators import FeedPageLocators
from page_objects.main_page import MainPage
import allure


class OrderFeedPage(MainPage):

    @allure.step("Переход на страницу ленты заказов")
    def go_to_feed_page(self):
        self.driver.get(ORDER_FEED_URL)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor_button(self):
        # Дождаться, пока кнопка "Конструктор" станет кликабельной
        self.wait_for_element_to_be_clickable(FeedPageLocators.CONSTRUCTOR_BUTTON)
        self.click_element_with_js(FeedPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Находим элемент заказа и кликаем по нему")
    def click_on_order(self):
        order_item = self.find_element(FeedPageLocators.FIRST_ORDER_ITEM)
        order_item.click()
        # Ожидаем появления модального окна
        self.wait_for_element_to_be_visible(FeedPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверяем, отображается ли модальное окно с деталями заказа")
    def is_order_modal_displayed(self):
        return self.is_element_visible(FeedPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click_element_with_js(FeedPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Находим элемент счётчика 'Выполнено за всё время' и возвращаем его текст в виде числа")
    def get_total_completed_orders_count(self):
        total_completed_element = self.find_element(FeedPageLocators.TOTAL_ORDERS_COMPLETED)
        return int(total_completed_element.text.strip())

    @allure.step("Находим элемент счётчика 'Выполнено за сегодня' и возвращаем его текст в виде числа")
    def get_daily_completed_orders_count(self):
        total_completed_element = self.find_element(FeedPageLocators.DAILY_ORDERS_COMPLETED)
        return int(total_completed_element.text.strip())

    @allure.step("Извлечение текста и преобразование его в целое число")
    def get_in_progress_order_numbers(self):
        # Ожидаем появления контейнера с заказами "В работе"
        self.wait_for_element_to_be_visible(FeedPageLocators.IN_PROGRESS_SECTION)
        # После появления контейнера извлекаем список элементов с номерами заказов
        order_elements = self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDER_NUMBER)
        # Извлекаем текст каждого элемента и преобразуем его в целое число
        order_numbers = [int(order.text.strip()) for order in order_elements]
        return order_numbers

    @allure.step("Ожидает, что номер заказа появится в разделе 'В работе'")
    def wait_for_order_number_in_progress(self, order_number, timeout=15):
        # Используем локатор для получения элементов
        order_number_locator = FeedPageLocators.IN_PROGRESS_ORDER_NUMBER

        try:
            # Ожидаем, что элемент будет появляться с таймаутом
            self.wait_for_element_to_appear(order_number_locator, timeout)

            # Получаем все номера заказов
            order_numbers = self.get_elements(order_number_locator)

            # Добавляем ведущий ноль к номеру заказа
            formatted_order_number = str(order_number).zfill(7)  # Предполагается, что номер всегда 7-значный

            # Проверяем наличие нужного номера заказа
            for element in order_numbers:
                if element.text.strip() == formatted_order_number:
                    return True

            # Если номер не найден, показываем исключение
            raise TimeoutException(f"Order number {formatted_order_number} did not appear in progress section.")

        except TimeoutException:
            raise TimeoutException(f"Order number {formatted_order_number} did not appear in the given timeout.")

    @allure.step("Проверяет, что указанный номер заказа отображается в истории заказов")
    def is_order_number_in_history(self, order_number):
        try:
            # Ожидание появления элементов с номерами заказов
            order_elements = self.wait_for_elements_visibility(FeedPageLocators.ORDER_HISTORY_NUMBER)

            # Получаем текст всех найденных номеров заказов
            found_numbers = [element.text.strip() for element in order_elements]

            # Проверяем, есть ли нужный номер в списке
            return any(order_number in element_text for element_text in found_numbers)

        except Exception as e:
            print("Ошибка при поиске номеров заказов в истории:", e)
            return False
