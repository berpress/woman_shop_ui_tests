"""Main page."""
from locators.main_page import MainPageLocators
from selenium.webdriver.common.keys import Keys


class MainPage:
    """Main page class."""

    def __init__(self, app):
        self.app = app

    def search_field(self):
        return self.app.wd.find_element(*MainPageLocators.SEARCH_FIELD)

    def negative_search_result(self):
        return self.app.wd.find_element(*MainPageLocators.NEGATIVE_SEARCH_RESULT).text

    def positive_search_result(self):
        return self.app.wd.find_element(*MainPageLocators.POSITIVE_SEARCH_RESULT).text

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

    def add_ro_cart_button(self):
        """Выбирает первый товар из списка элементов на главной странице."""
        return self.app.wd.find_elements(*MainPageLocators.ADD_TO_CART_BUTTONS)[0]

    def proceed_to_checkout_button(self):
        return self.app.wd.find_element(*MainPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
