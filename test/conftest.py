import pytest
from allure_commons._allure import attach
from allure import attachment_type
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as fOptions
import os

from page_objects.home import MainPage


def pytest_addoption(parser):
    parser.addoption("--firefox",
                     action='store_true',
                     default=False,
                     help="Start Firefox WebDriver")
    parser.addoption("--ie",
                     action='store_true',
                     default=False,
                     help="Start Internet Explorer WebDriver")
    parser.addoption("--google-chrome",
                     action='store_true',
                     default=False,
                     help="Start Google Chrome WebDriver")
    parser.addoption("--webdriver-location",
                     action='store',
                     help="Where to get the webdriver")
    parser.addoption("--correct-creds",
                     action='store',
                     help="Username and password to login to Diprella")
    parser.addoption("--incorrect-creds",
                     action='store',
                     help="Incorrect Username and Password to login to Diprella")
    parser.addoption("--user-info",
                     action='store',
                     help="Name, Surname, Email and Password to register in Diprella")



@pytest.fixture(scope='class', autouse=True)
def web_driver_setup(request):
    request.cls.webdriver_path = pytest.config.getoption("--webdriver-location")

    if pytest.config.getoption("--firefox"):
        request.cls.webdriver = webdriver.Firefox
    elif pytest.config.getoption("--ie"):
        request.cls.webdriver = webdriver.Ie
    elif pytest.config.getoption("--google-chrome"):
        request.cls.webdriver = webdriver.Chrome
    else:
        raise ValueError("Incorrect browser")


@pytest.fixture(scope='function', autouse=True)
def load_app(request):
    if isinstance(request.cls.webdriver, webdriver.Chrome):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        request.cls.initialized_webdriver = request.cls.webdriver(executable_path=request.cls.webdriver_path, chrome_options=chrome_options)
    elif isinstance(request.cls.webdriver, webdriver.Firefox):
        browser_profile = webdriver.FirefoxProfile()
        browser_profile.set_preference("dom.webnotifications.enabled", False)
        browser_profile.set_preference("dom.push"
                                        ".enabled", False)
        options = fOptions()
        #options.set_headless(headless=True)
        request.cls.initialized_webdriver = request.cls.webdriver(executable_path=request.cls.webdriver_path,
                                                                  firefox_options=options, firefox_profile=browser_profile)
    else:
        request.cls.initialized_webdriver = request.cls.webdriver(executable_path=request.cls.webdriver_path)
    request.cls.home = MainPage(request.cls.initialized_webdriver)
    def driver_close():
        request.cls.initialized_webdriver.quit()

    request.addfinalizer(driver_close)

def pytest_generate_tests(metafunc):
    creds_list = list()
    with open(os.path.join(os.path.abspath(os.path.curdir), 'correct-creds.txt'), 'r') as input_file:
        for line in input_file:
            vals = line.split(", ")
            creds_list.append((str(vals[0]), str(vals[1].strip())))
    metafunc.parametrize("username, password", tuple(creds_list))



#### Dealing with the test failure. Taking the page screenshot ###
def pytest_exception_interact(node, call, report):
    if report.failed:
        attach(
            node.instance.initialized_webdriver.get_screenshot_as_png(),
            name="Screenshot of the StackOverflow on test fail",
            attachment_type=attachment_type.PNG
