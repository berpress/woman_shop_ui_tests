from selenium.webdriver.common.by import By
from common.constants import MY_ACCOUNT


class RegistrationLocators:
    EMAIL = (By.ID, 'email_create')
    SIGN_IN_BUTTON = (By.CLASS_NAME, 'header_user_info')
    SUBMIT_CREATE = (By.ID, 'SubmitCreate')

    FIRST_NAME = (By.ID, 'customer_firstname')
    LAST_NAME = (By.ID, 'customer_lastname')
    PASSWORD = (By.ID, 'passwd')
    ADDRESS = (By.ID, 'address1')
    CITY = (By.ID, 'city')
    STATE = (By.XPATH, '//*[@id="id_state"]/option[2]')
    POSTAL_CODE = (By.ID, 'postcode')
    COUNTRY = (By.XPATH, '//*[@id="id_country"]/option[2]')
    MOBILE_PHONE = (By.ID, 'phone_mobile')
    ADDRESS_ALIAS = (By.ID, 'alias')
    REGISTER_BUTTON = (By.ID, 'submitAccount')

    MY_ACCOUNT = (By.XPATH, '//h1[text()="My account"]')
