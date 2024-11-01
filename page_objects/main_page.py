from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from data import BASE_URL, LOGIN_URL


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Переход на главную страницу")
    def go_to_main_page(self):
        self.driver.get(BASE_URL)

    @allure.step("Переход на страницу логина")
    def go_to_login_page(self):
        self.driver.get(LOGIN_URL)

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Java клик по элементу")
    def click_element_with_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание появления элемента")
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Проверка, что элемент виден на странице")
    def is_element_visible(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    @allure.step("Ожидание видимости элемента")
    def wait_for_element_to_be_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Поиск элемента")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Ввод текста")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()  # Очищает поле перед вводом текста
        element.send_keys(text)

    @allure.step("Ожидает, пока URL будет содержать указанный текст")
    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))

    @allure.step("Ожидание, что элемент станет кликабельным")
    def wait_for_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание, что элемент станет невидимым с таймаутом")
    def wait_for_element_to_be_invisible(self, locator, timeout=1):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Находит элемент на странице с ожиданием его видимости")
    def find_element(self, locator):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(locator),
            message=f"Не удалось найти элемент с локатором {locator}"
        )

    @allure.step("Возвращает все элементы, соответствующие заданному локатору")
    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ожидает, что элемент станет невидимым")
    def wait_for_element_invisibility(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Ожидает появления элемента на странице с таймаутом")
    def wait_for_element_to_appear(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Ожидает видимости всех элементов, найденных по локатору")
    def wait_for_elements_visibility(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
