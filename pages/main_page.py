"""Main page."""
from locators.main_page import MainPageLocators



class MainPage:
    """Класс главной страницы."""
    def __init__(self, app):
        self.app = app

    def sigh_in_button(self):
        """Вовзращает кнопкку SIGN IN."""
        return self.app.wd.find_element(*MainPageLocators.SIGN_IN_BUTTON)

    def contact_us_button(self):
        """Возвращает кнопку CONTACT US."""
        return self.app.wd.find_element(*MainPageLocators.CONTACT_US_BUTTON)

    def cart_button(self):
        """Возвращает кнопку cart button."""
        return self.app.wd.find_element(*MainPageLocators.CART_BUTTON)

    def woman_category(self):
        """Возвращает кнопку WOMAN"""
        return self.app.wd.find_element(*MainPageLocators.WOMAN_CATEGORY)

    def sigh_in_button_text(self):
        """Вовзвращает текст кнопки  SIGN IN"""
        return self.sigh_in_button().text

    def contact_us_text(self):
        """Вовзвращает текст кнопки CONTACT US """
        return self.contact_us_button().text

    def cart_button_text(self):
        """Вовзвращает текст кнопки CART """
        return self.cart_button().text

    def woman_category_text(self):
        """Вовзвращает текст кнопки  WOMAN """
        return self.woman_category().text