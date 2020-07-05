from selenium.webdriver.common.keys import Keys

from locators.main_page import MainPageLocators


class MainPage:
    def __init__(self, app):
        self.app = app

    def search_field(self):
        return self.app.wd.find_element(*MainPageLocators.SEARCH_FIELD)

    def search_result(self):
        return self.app.wd.find_element(*MainPageLocators.SEARCH_RESULT).is_displayed()

    def search(self, input_value):
        """Ввод значения в поле поиска и нажатие клавиши ENTER."""
        self.search_field().send_keys(input_value)
        self.search_field().send_keys(Keys.ENTER)


