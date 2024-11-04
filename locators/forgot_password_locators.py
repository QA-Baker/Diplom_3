from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name']")

    RESTORE_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Восстановить']")
