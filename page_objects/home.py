from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page_objects.login import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.signup import SignUpPage

class MainPage(object):
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        self.web_driver.maximize_window()
        self.web_driver.get("https://demo.diprella.com/")

    @property
    def enter_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header__nav-link")))

    @property
    def registration_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header__nav-button")))


    def click_on_enter_button(self):
        self.enter_button.click()
        return LoginPage(self.web_driver)

    def click_on_reg_button(self):
        self.registration_button.click()
        return SignUpPage(self.web_driver)

