from selenium.webdriver.common.by import By


class NewsLettersLocators:
    """Класс для констант"""

    INPUT_EMAIL_FIELD = (By.ID, 'newsletter-input')
    SEND_BUTTON = (By.NAME, "submitNewsletter")
