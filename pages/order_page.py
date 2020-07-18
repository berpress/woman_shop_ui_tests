from locators.order_page import OrderPageLocators
import re


class OrderPage:
    def __init__(self, app):
        self.app = app

    def summary_proceed_to_checkout(self):
        return self.app.wd.find_element(
            *OrderPageLocators.SUMMARY_PROCEED_TO_CHECKOUT_BUTTON
        ).click()

    def address_proceed_to_checkout(self):
        return self.app.wd.find_element(
            *OrderPageLocators.ADDRESS_PROCEED_TO_CHECKOUT_BUTTON
        ).click()

    def terms_checkbox_click(self):
        return self.app.wd.find_element(
            *OrderPageLocators.TERMS_OF_SERVICE_CHECKBOX
        ).click()

    def shipping_proceed_to_checkout(self):
        return self.app.wd.find_element(
            *OrderPageLocators.SHIPPING_PROCEED_TO_CHECKOUT_BUTTON
        ).click()

    def pay_by_check(self):
        return self.app.wd.find_element(*OrderPageLocators.PAY_BY_CHECK_BUTTON).click()

    def pay_by_bank_wire(self):
        return self.app.wd.find_element(
            *OrderPageLocators.PAY_BY_BANK_WIRE_BUTTON
        ).click()

    def confirm_order(self):
        return self.app.wd.find_element(*OrderPageLocators.CONFIRM_ORDER_BUTTON).click()

    def order_created_by_cheque(self):
        return self.app.wd.find_element(
            *OrderPageLocators.ORDER_CREATED_TEXT_BY_CHEQUE
        ).text

    def order_code_by_cheque(self):
        """В блоке информации о заказе находит код созданного заказа."""
        order_info = self.app.wd.find_element(
            *OrderPageLocators.ORDER_INFO_BY_CHEQUE
        ).text
        return re.findall(r"([A-Z]{9})", order_info)[0]

    def order_created_by_card(self):
        return self.app.wd.find_element(
            *OrderPageLocators.ORDER_CREATED_TEXT_BY_CARD
        ).text

    def order_code_by_card(self):
        """В блоке информации о заказе находит код созданного заказа."""
        order_info = self.app.wd.find_element(
            *OrderPageLocators.ORDER_INFO_BY_CARD
        ).text
        return re.findall(r"([A-Z]{9})", order_info)[0]

    def check_terms_of_use(self):
        driver = self.app.wd
        return driver.find_element(*OrderPageLocators.TERMS_OF_SERVICE_AGREEMENT).text

    def input_comment(self, text: str):
        driver = self.app.wd
        element = driver.find_element(*OrderPageLocators.COMMENT_FIELD)
        element.send_keys(text)
