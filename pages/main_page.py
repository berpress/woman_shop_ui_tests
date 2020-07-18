"""Main page."""
from locators.main_page import MainPageLocators
from selenium.webdriver.common.keys import Keys


class MainPage:
    """Main page class."""

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

    def sigh_in_button(self):
        return self.app.wd.find_element(*MainPageLocators.SIGN_IN_BUTTON)

    def contact_us_button(self):
        return self.app.wd.find_element(*MainPageLocators.CONTACT_US_BUTTON)

    def cart_button(self):
        return self.app.wd.find_element(*MainPageLocators.CART_BUTTON)

    def woman_category(self):
        return self.app.wd.find_element(*MainPageLocators.WOMAN_CATEGORY)

    def sigh_in_button_text(self):
        return self.sigh_in_button().text

    def contact_us_text(self):
        return self.contact_us_button().text

    def cart_button_text(self):
        return self.cart_button().text

    def woman_category_text(self):
        return self.woman_category().text

    def girl_in_black(self):
        return self.app.wd.find_element(*MainPageLocators.GIRL_IN_BLACK_DRESS)

    def click_on_girl_in_black(self):
        return self.girl_in_black().click()
