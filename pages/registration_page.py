from locators.registration import RegistrationLocators
from model.registration import RegistrationUserData
from common.utilities import fill_input


class RegistrationPage:
    def __init__(self, app):
        self.app = app

    def sign_in_page_button(self):
        return self.app.wd.find_element(*RegistrationLocators.SIGN_IN_BUTTON)

    def email_for_create_input(self):
        return self.app.wd.find_element(*RegistrationLocators.EMAIL)

    def submit_create_button(self):
        return self.app.wd.find_element(*RegistrationLocators.SUBMIT_CREATE)

    def first_name_input(self):
        return self.app.wd.find_element(*RegistrationLocators.FIRST_NAME)

    def last_name_input(self):
        return self.app.wd.find_element(*RegistrationLocators.LAST_NAME)

    def password_input(self):
        return self.app.wd.find_element(*RegistrationLocators.PASSWORD)

    def address_input(self):
        return self.app.wd.find_element(*RegistrationLocators.ADDRESS)

    def city_input(self):
        return self.app.wd.find_element(*RegistrationLocators.CITY)

    def state_list(self):
        return self.app.wd.find_element(*RegistrationLocators.STATE)

    def postal_code_input(self):
        return self.app.wd.find_element(*RegistrationLocators.POSTAL_CODE)

    def country_list(self):
        return self.app.wd.find_element(*RegistrationLocators.COUNTRY)

    def mobile_phone_input(self):
        return self.app.wd.find_element(*RegistrationLocators.MOBILE_PHONE)

    def address_alias_input(self):
        return self.app.wd.find_element(*RegistrationLocators.ADDRESS_ALIAS)

    def register_button_input(self):
        return self.app.wd.find_element(*RegistrationLocators.REGISTER_BUTTON)

    def my_account(self):
        return self.app.wd.find_elements(*RegistrationLocators.MY_ACCOUNT)

    def start_registration_process(self, user_data: RegistrationUserData):
        self.sign_in_page_button().click()
        self.email_for_create_input().send_keys(user_data.email)
        self.submit_create_button().click()

    # def fill_input(self, element, value):
    #     """Заполняет поле в зависимости от его типа и передаваемого значения"""
    #     if value:
    #         element().send_keys(value)
    #
    # def fill_requireds(self, user_data: RegistrationUserData):
    #     self.fill_input(self.first_name_input, user_data.first_name)
    #     self.fill_input(self.last_name_input, user_data.last_name)
    #     self.fill_input(self.password_input, user_data.password)
    #     self.fill_input(self.address_input, user_data.address)
    #     self.fill_input(self.city_input, user_data.city)
    #     self.state_list().click()
    #     self.fill_input(self.postal_code_input, user_data.postal_code)
    #     self.fill_input(self.mobile_phone_input, user_data.mobile_phone)
    #     self.register_button_input().click()

    def fill_requireds(self, user_data: RegistrationUserData):
        fill_input(self.first_name_input, user_data.first_name)
        fill_input(self.last_name_input, user_data.last_name)
        fill_input(self.password_input, user_data.password)
        fill_input(self.address_input, user_data.address)
        fill_input(self.city_input, user_data.city)
        self.state_list().click()
        fill_input(self.postal_code_input, user_data.postal_code)
        fill_input(self.mobile_phone_input, user_data.mobile_phone)
        self.register_button_input().click()

    def check_my_account(self):
        if len(self.my_account()) == 0:
            return False
        return True
