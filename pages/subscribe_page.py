import allure
import faker

from locators.subscribe import SubscribeLocators


class SubscribeFunction:
    """Класс с функциями для подписки на рассылку."""

    def __init__(self, app):
        self.app = app

    @allure.step("Ввод email в поле Newsletter и нажатие кнопки '>'")
    def email_subscribe(self, email: str) -> None:
        driver = self.app.wd
        element = driver.find_element(*SubscribeLocators.INPUT_EMAIL_FIELD)
        element.send_keys(email)
        element = driver.find_element(*SubscribeLocators.SEND_BUTTON)
        element.click()

    def check_success_alert(self) -> bool:
        return self.app.wd.find_element(*SubscribeLocators.SUCCESS_ALERT).is_displayed()

    def check_unsuccessful_alert(self) -> bool:
        return self.app.wd.find_element(
            *SubscribeLocators.INVALID_EMAIL_ALERT
        ).is_displayed()

    def generate_valid_email(self) -> str:
        fake = faker.Faker()
        valid_email = fake.email()
        return valid_email

    def email_subscribe_get_text(self) -> str:
        return self.success_alert().text

    def success_alert(self) -> str:
        return self.app.wd.find_element(*SubscribeLocators.SUCCESS_ALERT)

    def email_subscribe_get_text_with_error(self) -> str:
        return self.unsuccessful_alert().text

    def unsuccessful_alert(self) -> str:
        return self.app.wd.find_element(*SubscribeLocators.INVALID_EMAIL_ALERT)
