from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.login import LoginPage


class FBPage(object):
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver

    @property
    def not_now_button(self):
        return WebDriverWait(self.web_driver,40).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Not now')]")))

    def click_not_now_button(self):
        self.not_now_button.click()
        return LoginPage(self.web_driver)