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
        self.name_input = self.name_input.web_driver.find_element(By.XPATH,
                                        "/html/body/app-root/div/app-sign-up/section/div[3]/form/fieldset/div[1]/fieldset[1]/input")
        self.password_input = self.password_input.web_driver.find_element(By.XPATH,
                                        "/html/body/app-root/div/app-sign-up/section/div[3]/form/fieldset/div[2]/div/fieldset/input")
        self.mail_input = self.mail_input.web_driver.find_element(By.XPATH,
                                        "/html/body/app-root/div/app-sign-up/section/div[3]/form/fieldset/div[2]/fieldset/input")
        self.surname_input = self.surname_input.web_driver.find_element(By.XPATH,
                                        "/html/body/app-root/div/app-sign-up/section/div[3]/form/fieldset/div[1]/fieldset[2]/input")

    @property
    def diprella_logo(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-sign-up/section/a/div")))

    @property
    def regisration_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-sign-up/section/div[3]/form/button")))

    @property
    def fb_login_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/app-root/div/app-sign-up/section/div[3]/nav/app-fb-auth/a")))

    @property
    def google_login_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='googleButton']")))

    @property
    def in_login_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/app-root/div/app-sign-up/section/div[3]/nav/app-ln-auth/a")))


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

    def click_on_registration_button(self):
        self.regisration_button.click()
        return UserWorkspacePage(self.web_driver)
