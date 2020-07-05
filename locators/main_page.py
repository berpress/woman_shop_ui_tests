"""Локаторы для глввной страницы."""
from selenium.webdriver.common.by import By


class MainPageLocators:
    SIGN_IN_BUTTON = (By.CLASS_NAME, 'login')
    CONTACT_US_BUTTON = (By.ID, 'contact-link')
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart')
    WOMAN_CATEGORY = (By.CLASS_NAME, 'sf-with-ul')