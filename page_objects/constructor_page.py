from data import BASE_URL
from locators.constructor_page_locators import ConstructorPageLocators
from page_objects.main_page import MainPage
import allure


class ConstructorPage(MainPage):

    @allure.step("Проверка нахождения на странице конструктора")
    def is_on_constructor_page(self):
        # Проверка, что текущий URL соответствует главной странице (конструктору)
        return self.driver.current_url.rstrip('/') == BASE_URL.rstrip('/')

    @allure.step("Клик по указанному ингредиенту")
    def click_ingredient(self, ingredient_locator):
        self.click_element(ingredient_locator)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_place_order_button(self):
        self.click_element(ConstructorPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Переход на страницу конструктора")
    def go_to_constructor_page(self):
        self.click_element_with_js(ConstructorPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Метод для клика по ингредиенту и открытия всплывающего окна с деталями")
    def click_ingredient(self, ingredient_locator):
        self.click_element(ingredient_locator)

    @allure.step("Проверяет, отображается ли модальное окно")
    def is_modal_displayed(self):
        return self.is_element_visible(ConstructorPageLocators.MODAL_WINDOW)

    @allure.step("Закрывает модальное окно")
    def close_modal(self):
        close_button = self.find_element(ConstructorPageLocators.MODAL_CLOSE_BUTTON)
        close_button.click()

    @allure.step("Возвращает текущее значение счётчика указанного ингредиента")
    def get_ingredient_counter(self, ingredient_locator):
        ingredient = self.find_element(ingredient_locator)
        counter = ingredient.find_element(*ConstructorPageLocators.INGREDIENT_COUNTER)
        return int(counter.text)

    @allure.step("drag and drop который работает в Mozilla")
    def drag_and_drop_ingredient(self, ingredient_element, target_area_element):
        script = """
        function createEvent(typeOfEvent) {
            var event = document.createEvent('CustomEvent');
            event.initCustomEvent(typeOfEvent, true, true, null);
            event.dataTransfer = {
                data: {},
                setData: function(key, value) { this.data[key] = value; },
                getData: function(key) { return this.data[key]; }
            };
            return event;
        }

        function dispatchEvent(element, event, transferData) {
            if (transferData !== undefined) {
                event.dataTransfer = transferData;
            }
            if (element.dispatchEvent) {
                element.dispatchEvent(event);
            } else if (element.fireEvent) {
                element.fireEvent('on' + event.type, event);
            }
        }

        function simulateHTML5DragAndDrop(element, dropzone) {
            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(element, dragStartEvent);
            var dragEnterEvent = createEvent('dragenter');
            dispatchEvent(dropzone, dragEnterEvent, dragStartEvent.dataTransfer);
            var dragOverEvent = createEvent('dragover');
            dispatchEvent(dropzone, dragOverEvent, dragStartEvent.dataTransfer);
            var dropEvent = createEvent('drop');
            dispatchEvent(dropzone, dropEvent, dragStartEvent.dataTransfer);
            var dragEndEvent = createEvent('dragend');
            dispatchEvent(element, dragEndEvent);
        }

        simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, ingredient_element, target_area_element)

    @allure.step("Проверяет, что заказ успешно оформлен по наличию подтверждения")
    def is_order_successful(self):
        return self.is_element_visible(ConstructorPageLocators.ORDER_CONFIRMATION)

    @allure.step("Возвращает название ингредиента из модального окна")
    def get_modal_ingredient_name(self):
        return self.find_element(ConstructorPageLocators.MODAL_INGREDIENT_NAME).text

    @allure.step("Получает локатор конкретного ингредиента и области конструктора")
    def get_element(self, locator):
        return self.find_element(locator)
