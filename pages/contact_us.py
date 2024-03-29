from typing import Any

from common.utilities import fill_input
import allure

from locators.contact_us import ContactUsLocators
from model.contact_us import ContactUsUserData


class ContactUsForm:
    """Класс с функция для страницы Contact us."""

    def __init__(self, app):
        self.app = app

    @allure.step("Нажатие кнопки contact us на главной странице")
    def find_and_click_contact_us_button(self) -> str:
        return self.app.wd.find_element(*ContactUsLocators.CONTACT_US_LINK).click()

    @allure.step("Выбор предметного указателя Customer service в Subject Heading")
    def click_on_subject_heading_button(self) -> None:
        driver = self.app.wd
        element = driver.find_element(*ContactUsLocators.SUBJECT_HEADING)
        element.find_element_by_xpath("//option[text()='Customer service']").click()


    @allure.step("Ввод email  в поле Email address")
    def click_on_email_field(self, email: str) -> None:
        driver = self.app.wd
        element = driver.find_element(*ContactUsLocators.EMAIL_ADDRESS)
        element.send_keys(email)

    @allure.step("Ввод текста в поле Order reference")
    def click_on_order_reference_field(self, text: str) -> None:
        driver = self.app.wd
        element = driver.find_element(*ContactUsLocators.ORDER_REFERENCE)
        element.send_keys(text)

    @allure.step("Нажатие кнопки Choose File")
    def click_on_choose_file(self, path):
        driver = self.app.wd
        element = driver.find_element(*ContactUsLocators.CHOOSE_FILE_BUTTON)
        element.send_keys(path)


    def choose_file_for_upload(self):  # заготовка
        pass

    @allure.step("Ввод текста в поле сообщения")
    def input_message_text(self, text: str) -> None:
        driver = self.app.wd
        element = driver.find_element(*ContactUsLocators.MESSAGE_INPUT_FILED)
        element.send_keys(text)

    @allure.step("Нажатие кнопки отправить")
    def click_in_send_button(self) -> None:
        driver = self.app.wd
        element = driver.find_element(*ContactUsLocators.SEND_MESSAGE_BUTTON)
        element.click()

    def check_success_alert(self) -> bool:
        return self.app.wd.find_element(*ContactUsLocators.SUCCESS_ALERT).is_displayed()

    def check_unsuccessful_alert(self) -> bool:
        return self.app.wd.find_element(
            *ContactUsLocators.INVALID_EMAIL_ALERT
        ).is_displayed()

    def get_text_from_success_alert(self) -> str:
        return self.success_alert().text

    def success_alert(self) -> str:
        return self.app.wd.find_element(*ContactUsLocators.SUCCESS_ALERT)

    def get_text_from_alert_with_error(self) -> str:
        return self.unsuccessful_alert().text

    def unsuccessful_alert(self) -> str:
        return self.app.wd.find_element(*ContactUsLocators.INVALID_EMAIL_ALERT)

    def click_on_email_field(self) -> Any:
        driver = self.app.wd
        return driver.find_element(*ContactUsLocators.EMAIL_ADDRESS)

    def click_on_order_reference_field(self) -> str:
        driver = self.app.wd
        return driver.find_element(*ContactUsLocators.ORDER_REFERENCE)

    def input_message_text(self) -> str:
        driver = self.app.wd
        return driver.find_element(*ContactUsLocators.MESSAGE_INPUT_FILED)

    def click_in_send_button(self) -> None:
        driver = self.app.wd
        driver.find_element(*ContactUsLocators.SEND_MESSAGE_BUTTON).click()

    def fill_data(self, user_data: ContactUsUserData) -> None:
        fill_input(self.click_on_email_field, user_data.email)
        fill_input(self.click_on_order_reference_field, user_data.text)
        fill_input(self.input_message_text, user_data.text_in_form)
