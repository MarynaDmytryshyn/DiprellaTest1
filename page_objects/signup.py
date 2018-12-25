from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.user_workspace import UserWorkspacePage

class SignUpPage(object):
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver


    @property
    def name_input(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"[formcontrolname=first_name]")))

    @property
    def password_input(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"[formcontrolname=password]")))

    @property
    def mail_input(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"[formcontrolname=email]")))

    @property
    def surname_input(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"[formcontrolname=last_name]")))

    @property
    def diprella_logo(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-logo")))

    @property
    def regisration_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login__form-btn.dark__btn--hover")))

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
            EC.presence_of_element_located((By.CSS_SELECTOR, ".social__icons-box-link.linkedin")))

    @property
    def terms_checkbox(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "terms")))


    def enter_name(self, name):
        self.name_input.send_keys(name)
        return self

    def enter_surname(self, surname):
        self.surname_input.send_keys(surname)
        return self

    def enter_password(self, password):
        self.password_input.send_keys(password)
        return self

    def enter_email(self,email):
        self.mail_input.send_keys(email)
        return self

    def click_on_terms_checkbox(self):
        self.terms_checkbox.click()
        return self

    def click_on_registration_button(self):
        self.regisration_button.click()
        return UserWorkspacePage(self.web_driver)
