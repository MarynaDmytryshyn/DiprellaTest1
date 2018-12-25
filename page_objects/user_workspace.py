from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class UserWorkspacePage(object):
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver

    @property
    def diprella_logo(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header__logo")))

    @property
    def courses_search(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.ID, "search")))

    @property
    def instructor_menu(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Лектор')]")))

    @property
    def home_tab(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-link.active")))

    @property
    def bookmarks_tab(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "nav-link")))

    @property
    def profile_tab(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-link.ng-star-inserted")))

    @property
    def recommended_courses(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Рекомендації')]")))

    @property
    def popular_courses(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Популярні курси')]")))

    @property
    def library_menu(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "library__text")))

    @property
    def footer(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "footer__logo-rights")))

    @property
    def language_selector(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-dropdown-trigger.ui-state-default.ui-corner-right")))

    @property
    def donate_button(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".footer__nav-link.footer__nav-link_button")))

    @property
    def contact_us(self):
        return WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "footer__nav")))

