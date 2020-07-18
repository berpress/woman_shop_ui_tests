from selenium.webdriver.common.by import By


class SubscribeLocators:
    """Класс для констант"""

    INPUT_EMAIL_FIELD = (By.ID, 'newsletter-input')
    SEND_BUTTON = (By.NAME, "submitNewsletter")
    SUCCESS_ALERT = (By.XPATH, '//*[@class="alert alert-success"]')
    INVALID_EMAIL_ALERT = (By.XPATH, '//*[@class="alert alert-danger"]')
