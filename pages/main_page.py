"""Main page."""

import allure
from selenium.webdriver import ActionChains

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

    @allure.step("Ввод значения в поле поиска")
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

    @allure.step("girl in black :D")
    def click_on_girl_in_black(self):
        return self.girl_in_black().click()


    @allure.step("Нажатие кнопки add to cart для первого товара на главной странице")
    def add_to_cart_button(self):
        """Выбирает первый товар из списка элементов на главной странице."""
        elem = self.app.wd.find_elements(*MainPageLocators.ADD_TO_CART_BUTTONS)[0]
        return elem.click()

    @allure.step("Наведение мышкой на первый товар на главной странице")
    def focus_first_good(self):
        """Наводит мышкой на первый товар из списка элементов на главной странице."""
        actions = ActionChains(self.app.wd)
        elem = self.app.wd.find_elements(*MainPageLocators.FIRST_GOOD_ON_MAIN_PAGE)[0]
        actions.move_to_element(elem).perform()

    @allure.step("Нажатие кнопки proceed to checkout")
    def proceed_to_checkout_button(self):
        elem = self.app.wd.find_element(*MainPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        return elem.click()
