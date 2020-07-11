from locators.subscribe import SubscribeLocators


class SubscribeFunction:
    """Класс с функциями для подписки на рассылку."""

    def __init__(self, app):
        self.app = app
#    def email_subscribe(self, email: str) -> None:

    def email_subscribe(self, email) -> None:
        driver = self.app.wd
        element = driver.find_element(*SubscribeLocators.INPUT_EMAIL_FIELD)
        element.send_keys(email)
        element = driver.find_element(*SubscribeLocators.SEND_BUTTON)
        element.click()

    def check_success_alert(self) -> bool:
        return self.app.wd.find_element(*SubscribeLocators.SUCCESS_ALERT).is_displayed()

    def check_unsuccessful_alert(self) -> bool:
        return self.app.wd.find_element(*SubscribeLocators.INVALID_EMAIL_ALERT).is_displayed()

    # def email_subscribe_get_text(self):
    #     return self.success_alert().text
    #
    # def email_subscribe_get_text_1(self):
    #     return self.unsuccessful_alert().text
    #
    # def success_alert(self):
    #     return self.app.wd.find_element(*SubscribeLocators.SUCCESS_ALERT)
    #
    # def unsuccessful_alert(self):
    #     return self.app.wd.find_element(*SubscribeLocators.INVALID_EMAIL_ALERT)
