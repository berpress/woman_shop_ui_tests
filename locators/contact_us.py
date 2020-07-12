from selenium.webdriver.common.by import By


class ContactUsLocators:
    """Константы для формы Contact us."""

    CONTACT_US_LINK = (By.ID, "contact-link")
    SUBJECT_HEADING = (By.ID, "id_contact")
    EMAIL_ADDRESS = (By.ID, "email")
    ORDER_REFERENCE = (By.NAME, "id_order")
    CHOOSE_FILE_BUTTON = (By.ID, "uniform-fileUpload")
    MESSAGE_INPUT_FILED = (By.ID, "message")
    SEND_MESSAGE_BUTTON = (By.ID, "submitMessage")
    SUCCESS_ALERT = (By.XPATH, '//*[@class="alert alert-success"]')
    INVALID_EMAIL_ALERT = (By.XPATH, '//*[@class="alert alert-danger"]')
