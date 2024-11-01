from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    CODE_INPUT_LABEL = (By.XPATH, "//label[text()='Введите код из письма']")

    PASSWORD_INPUT = (By.XPATH,
                      "//input[@class='text input__textfield text_type_main-default' and @name='Введите новый пароль']")

    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.input__icon-action")
