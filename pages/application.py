import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.contact_us import ContactUsForm
from pages.goods_page import GoodsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.my_account_page import My_Account_page
from pages.my_store_page import MyStorePage
from pages.order_page import OrderPage
from pages.registration_page import RegistrationPage
from pages.subscribe_page import SubscribeFunction


class Application:
    def __init__(self, base_url, headless):
        driver_path = ChromeDriverManager().install()
        options: Options = Options()
        options.headless = headless
        self.wd = webdriver.Chrome(driver_path, options=options)
        self.base_url = base_url
        self.order_history_url = (
            "http://automationpractice.com/index.php?controller" "=history"
        )
        self.login = LoginPage(self)
        self.newsletter = SubscribeFunction(self)
        self.main_page = MainPage(self)
        self.my_account = My_Account_page(self)
        self.my_store = MyStorePage(self)
        self.goods_page = GoodsPage(self)
        self.order_page = OrderPage(self)
        self.registration = RegistrationPage(self)
        self.contact_us = ContactUsForm(self)

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.wd.get(self.base_url)

    @allure.step("Открытие страницы wishlist")
    def open_wishlist(self):
        self.wd.get(
            self.base_url
            + "index.php?fc=module&module=blockwishlist&controller=mywishlist"
        )

    @allure.step("Открытие страницы истории заказов")
    def open_order_history_page(self):
        self.wd.get(self.order_history_url)

    def get_page_source(self):
        return self.wd.page_source
