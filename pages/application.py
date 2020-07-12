from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.subscribe_page import SubscribeFunction


class Application:
    def __init__(self, base_url):
        driver_path = ChromeDriverManager().install()
        options: Options = Options()
        options.headless = True
        self.wd = webdriver.Chrome(driver_path, options=options)
        self.base_url = base_url
        self.login = LoginPage(self)
        self.newsletter = SubscribeFunction(self)
        self.main_page = MainPage(self)
        self.registration = RegistrationPage(self)

    def open_main_page(self):
        self.wd.get(self.base_url)
