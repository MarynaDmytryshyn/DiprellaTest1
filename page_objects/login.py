from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.user_workspace import UserWorkspacePage

class LoginPage(object):
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        self.username_input = self.username_input.web_driver.find_element(By.XPATH,
                                                    "/html/body/app-root/div/app-auth/section/div[1]/form/fieldset/fieldset/input")
        self.password_input = self.password_input.web_driver.find_element(By.XPATH,
                                                    "/html/body/app-root/div/app-auth/section/div[1]/form/fieldset/div/fieldset/input")

    @property
    def diprella_logo(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-auth/section/a/div")))

    @property
    def enter_regisration_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-auth/section/div[2]/a/div")))

    @property
    def fb_login_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-auth/section/div[1]/nav/app-fb-auth/a")))

    @property
    def google_login_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='googleButton']")))

    @property
    def in_login_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/app-root/div/app-auth/section/div[1]/nav/app-ln-auth/a")))

    @property
    def login_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/app-root/div/app-auth/section/div[1]/form/button")))



    def enter_username(self,username):
        self.username_input.send_keys(username)
        return self

    def enter_password(self,password):
        self.password_input.send_keys(password)
        return self

    def click_on_login_button(self):
        self.login_button.click()
        return UserWorkspacePage(self.web_driver)

    def click_on_login_button_negative(self):
        self.login_button.click()
        return self
