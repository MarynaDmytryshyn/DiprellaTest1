from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class UserWorkspacePage(object):
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver