from selenium.webdriver.common.by import By

from locators.subscribe import NewsLettersLocators
from selenium.common.exceptions import NoSuchElementException


class SubscribeFunction:
    def __init__(self, app):
        self.app = app

    def input_email(self, email: str) -> None:
        """Ввод email."""
        driver = self.app.wd
        element = driver.find_element(*NewsLettersLocators.INPUT_EMAIL_FIELD)
        element.send_keys(email)

    def submit_subscribe(self) -> None:
        """Клик по кнопке 'подписаться'."""
        driver = self.app.wd
        element = driver.find_element(*NewsLettersLocators.SEND_BUTTON)
        element.click()

    def get_page(self) -> None:
        """Получение все страницы."""
        return self.app.wd.page_source()

    def check_exists_by_class_name(self, class_name) -> int:
        try:
            self.app.wd.find_element(By.CLASS_NAME, class_name)
            return 1
        except NoSuchElementException:
            return 0
