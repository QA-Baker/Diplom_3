from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password']")

    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")

    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
