from locators.registration_locators import RegistrationLocators
import allure


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

    @allure.step("Подготовка к регистрации - ввод емейла")
    def start_registration_process(self, user_data):
        self.sign_in_page_button().click()
        self.email_for_create_input().send_keys(user_data.email)
        self.submit_create_button().click()

    def fill_input(self, element, value):
        """Заполняет поле, если было передано значение value."""
        if value:
            element().send_keys(value)

    def fill_select(self, element, value):
        """Выбирает селект, если было передано значение value."""
        if value:
            element().click()

    @allure.step("Заполнение полей, которым были переданы данные")
    def fill_requireds(self, user_data):
        self.fill_input(self.first_name_input, user_data.first_name)
        self.fill_input(self.last_name_input, user_data.last_name)
        self.fill_input(self.password_input, user_data.password)
        self.fill_input(self.address_input, user_data.address)
        self.fill_input(self.city_input, user_data.city)
        self.fill_select(self.state_list, user_data.state)
        self.fill_input(self.postal_code_input, user_data.postal_code)
        self.fill_input(self.mobile_phone_input, user_data.mobile_phone)
        self.register_button_input().click()

    def check_my_account(self):
        if len(self.my_account()) == 0:
            return False
        return True
