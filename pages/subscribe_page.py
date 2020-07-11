from locators.subscribe import NewsLettersLocators


class SubscribeFunction:
    """Класс с функциями для подписки на рассылку."""

    def __init__(self, app):
        self.app = app

    def input_email_and_submit_subscribe(self, email: str) -> None:
        driver = self.app.wd
        element = driver.find_element(*NewsLettersLocators.INPUT_EMAIL_FIELD)
        element.send_keys(email)
        element = driver.find_element(*NewsLettersLocators.SEND_BUTTON)
        element.click()

    def check_success_alert(self) -> bool:
        return self.app.wd.find_element(*NewsLettersLocators.SUCCESS_ALERT).is_displayed()
