import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.goods_page import GoodsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.my_account_page import My_Account_page
from pages.my_store_page import MyStorePage
from pages.order_page import OrderPage
from pages.registration_page import RegistrationPage
from pages.subscribe_page import SubscribeFunction
from pages.woman_category_page import WomanCategoryPage


class Application:
    def __init__(self, base_url, headless):
        driver_path = ChromeDriverManager().install()
        options: Options = Options()
        options.headless = headless
        self.wd = webdriver.Chrome(driver_path, options=options)
        self.base_url = base_url
        self.login = LoginPage(self)
        self.newsletter = SubscribeFunction(self)
        self.main_page = MainPage(self)
        self.my_account = My_Account_page(self)
        self.my_store = MyStorePage(self)
        self.goods_page = GoodsPage(self)
        self.order_page = OrderPage(self)
        self.registration = RegistrationPage(self)
        self.woman_category = WomanCategoryPage(self)

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.wd.get(self.base_url)

    def open_wishlist(self):
        self.wd.get(
            self.base_url
            + "index.php?fc=module&module=blockwishlist&controller=mywishlist"
        )

    def open_order_history_page(self):
        self.wd.get(self.base_url + "index.php?controller" "=history")

    def open_woman_category_page(self):
        self.wd.get(self.base_url + "index.php?id_category=3&controller=category")

    def get_page_source(self):
        return self.wd.page_source
