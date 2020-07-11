from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.subscribe_page import SubscribeFunction



class Application:
    def __init__(self, base_url):
        driver_path = ChromeDriverManager().install()
        self.wd = webdriver.Chrome(driver_path)
        self.base_url = base_url
        self.login = LoginPage(self)
        self.newsletter = SubscribeFunction(self)
        self.main_page = MainPage(self)


    def open_main_page(self):
        self.wd.get(self.base_url)
