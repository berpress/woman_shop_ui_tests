"""Main page."""
from locators.main_page import MainPageLocators



class MainPage:
    """Main page class."""
    def __init__(self, app):
        self.app = app

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