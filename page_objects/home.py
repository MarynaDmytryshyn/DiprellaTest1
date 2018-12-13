from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page_objects.login import LoginPage

class MainPage(object):
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        self.web_driver.maximize_window()
        self.web_driver.get("https://demo.diprella.com/")

        self.enter_button = self.enter_button.web_driver.find_element(By.XPATH,
                                    "/html/body/app-root/div/app-home/section/section/app-header/header/div/section/div[2]/section/nav/a")

    def click_on_enter_button(self):
        self.enter_button.click()
        return LoginPage(self.web_driver)