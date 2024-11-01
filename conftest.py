from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        service = ChromeService(executable_path='D:/Программы/WebDriver/bin/chromedriver.exe')
        options = webdriver.ChromeOptions()
        browser = webdriver.Chrome(service=service, options=options)
    elif request.param == "firefox":
        service = FirefoxService(executable_path='D:/Программы/WebDriver/bin/geckodriver.exe')
        options = webdriver.FirefoxOptions()
        options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"  # Укажите путь к Firefox
        browser = webdriver.Firefox(service=service, options=options)

    yield browser
    browser.quit()
