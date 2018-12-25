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

    @property
    def username_input(self):
        return WebDriverWait(self.web_driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    "[formcontrolname=email]")))

    @property
    def password_input(self):
        return WebDriverWait(self.web_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    "[formcontrolname=password]")))

    @property
    def diprella_logo(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-logo")))

    @property
    def enter_regisration_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login__image-container-btn.white--btn--hover")))

    @property
    def fb_login_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".social__icons-box-link.facebook")))

    @property
    def google_login_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='googleButton']")))

    @property
    def in_login_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".social__icons-box-link.linkedin")))

    @property
    def login_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".login__form-btn.dark__btn--hover")))


    @property
    def error_message(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".error__text")))

    @property
    def sign_in_text(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".login__content-title")))

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


