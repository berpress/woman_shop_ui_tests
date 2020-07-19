from selenium.webdriver.common.keys import Keys
from locators.goods_page import GoodsPageLocators


class GoodsPage:
    def __init__(self, app):
        self.app = app

    def add_to_wishlist_button(self):
        return self.app.wd.find_element(*GoodsPageLocators.ADD_TO_WISHLIST_BUTTON)

    def close_fancy_box_button(self):
        return self.app.wd.find_element(*GoodsPageLocators.CLOSE_FANCY_BOX)

    def add_to_cart_button(self):
        return self.app.wd.find_element(*GoodsPageLocators.ADD_TO_CART)

    def add_successfull_additional_to_cart(self):
        return self.app.wd.find_element(*GoodsPageLocators.SUCCESSFULL_ADD_TO_CART)

    def text_of_successfull_additional(self):
        return self.add_successfull_additional_to_cart().text

    def click_on_add_to_wishlist(self):
        return self.add_to_wishlist_button().click()

    def click_on_fancy_box_button(self):
        return self.close_fancy_box_button().click()

    def quantity_field(self):
        return self.app.wd.find_element(*GoodsPageLocators.QUANTITY_FIELD)

    def quantity_field_plus_button(self):
        return self.app.wd.find_element(*GoodsPageLocators.QUANTITY_PLUS_BUTTON)

    def quantity_field_minus_button(self):
        return self.app.wd.find_element(*GoodsPageLocators.QUANTITY_MINUS_BUTTON)

    def send_keys_to_quantity_filed(self, text):
        self.quantity_field().send_keys(Keys.BACKSPACE)
        return self.quantity_field().send_keys(text)

    def click_on_quantity_field_plus_button(self):
        return self.quantity_field_plus_button().click()

    def click_on_quantity_field_minus_button(self):
        return self.quantity_field_minus_button().click()

    def click_add_to_cart_button(self):
        return self.add_to_cart_button().click()