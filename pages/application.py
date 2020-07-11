from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


class Application:
    def __init__(self, base_url):
        options: Options = Options()
        options.headless = True
        driver_path = ChromeDriverManager().install()
        self.wd = webdriver.Chrome(driver_path, options=options)
        self.base_url = base_url
        self.login = LoginPage(self)

    def open_main_page(self):
        self.wd.get(self.base_url)
