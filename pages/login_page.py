import allure
import logging

from common.Login_Constants import AutorizedUser
from locators.login import LoginLocators
from model.login import UserData

logger = logging.getLogger()


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

    def logout_button(self):
        return self.app.wd.find_element(*LoginLocators.LOGOUT_BUTTON)

    def logout_button_click(self):
        self.logout_button().click()

    def login_button_get_text(self):
        return self.login_button().text

    def submit_login(self):
        return self.app.wd.find_element(*LoginLocators.SUBMIT_BUTTON)

    def login_auth_alert(self):
        return self.app.wd.find_element(*LoginLocators.AUTH_ALERT)

    def login_auth_alert_get_text(self):
        return self.login_auth_alert().text

    @allure.step("Авторизация")
    def auth(self, user_data: UserData, is_submit=True):
        logger.info(f'Try to login with login: {user_data.login} and password: '
                    f'{user_data.password}')
        """
        :param user_data: Class UserData, attribuites (Login: str, Password: str)
        :param is_submit: Attribuit, Boolean
        """
        if self.app.login.login_button_get_text() == AutorizedUser.AUTH_USER:
            self.logout_button_click()
            self.login_button_click()
        else:
            self.login_button_click()
        if user_data.login is not None:
            self.email_input().send_keys(user_data.login)
        if user_data.password is not None:
            self.password_input().send_keys(user_data.password)
        if is_submit:
            self.submit_login().click()

    @allure.step("Выход из аккаунта")
    def logout_if_logged_in(self):
        if self.app.wd.find_elements(*LoginLocators.LOGOUT_BUTTON):
            self.logout_button_click()
