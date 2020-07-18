from locators.login import LoginLocators
from model.login import UserData


class LoginPage:
    def __init__(self, app):
        self.app = app

    def email_input(self):
        return self.app.wd.find_element(*LoginLocators.LOGIN_INPUT)

    def password_input(self):
        return self.app.wd.find_element(*LoginLocators.PASSWORD_INPUT)

    def login_button(self):
        return self.app.wd.find_element(*LoginLocators.LOGIN_BUTTON)

    def login_button_click(self):
        self.login_button().click()

    def login_button_get_text(self):
        return self.login_button().text

    def submit_login(self):
        return self.app.wd.find_element(*LoginLocators.SUBMIT_BUTTON)

    def login_auth_alert(self):
        return self.app.wd.find_element(*LoginLocators.AUTH_ALERT)

    def login_auth_alert_get_text(self):
        return self.login_auth_alert().text

    def auth(self, user_data: UserData, is_submit=True):
        """
        :param user_data: Class UserData, attribuites (Login: str, Password: str)
        :param is_submit: Attribuit, Boolean
        """
        self.login_button_click()
        if user_data.login is not None:
            self.email_input().send_keys(user_data.login)
        if user_data.password is not None:
            self.password_input().send_keys(user_data.password)
        if is_submit:
            self.submit_login().click()
