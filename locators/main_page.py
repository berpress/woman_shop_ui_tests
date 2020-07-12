"""Main page locators."""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Class for Main page Locators."""
    SIGN_IN_BUTTON = (By.CLASS_NAME, 'login')
    CONTACT_US_BUTTON = (By.ID, 'contact-link')
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart')
    WOMAN_CATEGORY = (By.CLASS_NAME, 'sf-with-ul')
    SEARCH_FIELD = (By.ID, 'search_query_top')
    SEARCH_RESULT = (By.XPATH, '//span[@class="heading-counter"]')
    GIRL_IN_BLACK_DRESS = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[1]")