from selenium.webdriver.common.keys import Keys

import allure


from common.constants import SUCCESS_ADD_TO_CART_TEXT
from locators.goods_page import GoodsPageLocators


class GoodsPage:
    def __init__(self, app):
        self.app = app

    def add_to_wishlist_button(self):
        return self.app.wd.find_element(*GoodsPageLocators.ADD_TO_WISHLIST_BUTTON)

    @allure.step("Закрытие модального окна")
    def close_fancy_box_button(self):
        return self.app.wd.find_element(*GoodsPageLocators.CLOSE_FANCY_BOX)

    def close_modal_window_button(self):
        return self.app.wd.find_element(*GoodsPageLocators.CLOSE_POP_UP)

    def add_to_cart_button(self):
        return self.app.wd.find_element(*GoodsPageLocators.ADD_TO_CART)

    def add_successfull_additional_to_cart(self):
        return self.app.wd.find_element(*GoodsPageLocators.SUCCESSFULL_ADD_TO_CART)

    def text_of_successfull_additional(self):
        if self.app.wait_until_text_in_element(
            GoodsPageLocators.SUCCESSFULL_ADD_TO_CART, SUCCESS_ADD_TO_CART_TEXT
        ):
            return self.add_successfull_additional_to_cart().text

    @allure.step("Закрытие окна успешного добавления товара в корзину")
    def click_on_close_window_button(self):
        return self.close_modal_window_button().click()

    def quantity_in_cart(self):
        return self.app.wd.find_element(*GoodsPageLocators.NUMBER_IN_CART)

    def quantity_in_cart_text(self):
        return self.quantity_in_cart().text

    @allure.step("Нажатие кнопки Add to wishlist")
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

    @allure.step("Ввод числа в поле количества товара")
    def send_keys_to_quantity_filed(self, text):
        self.quantity_field().send_keys(Keys.BACKSPACE)
        return self.quantity_field().send_keys(text)

    @allure.step("Увеличение количества товара в корзине на 1 единицу")
    def click_on_quantity_field_plus_button(self):
        return self.quantity_field_plus_button().click()

    @allure.step("Уменьшение количества товара в корзине на 1 единицу")
    def click_on_quantity_field_minus_button(self):
        return self.quantity_field_minus_button().click()

    @allure.step("Нажатие кнопки add to cart")
    def click_add_to_cart_button(self):
        return self.add_to_cart_button().click()
