"""Main page locators."""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Class for Main page Locators."""

    SIGN_IN_BUTTON = (By.CLASS_NAME, "login")
    CONTACT_US_BUTTON = (By.ID, "contact-link")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart")
    WOMAN_CATEGORY = (By.CLASS_NAME, "sf-with-ul")
    SEARCH_FIELD = (By.ID, "search_query_top")
    SEARCH_RESULT = (By.XPATH, '//span[@class="heading-counter"]')
    GIRL_IN_BLACK_DRESS = (By.PARTIAL_LINK_TEXT, "Blou")
    NEGATIVE_SEARCH_RESULT = (By.XPATH, '//p[@ class = "alert alert-warning"]')
    POSITIVE_SEARCH_RESULT = (By.XPATH, '//span[@class = "lighter"]')
    ADD_TO_CART_BUTTONS = (
        By.XPATH,
        '//a[@class = "button ajax_add_to_cart_button btn btn-default"]',
    )
    FIRST_GOOD_ON_MAIN_PAGE = (By.XPATH, '//div[@class="product-image-container"]')
    PROCEED_TO_CHECKOUT_BUTTON = (
        By.XPATH,
        '//a[@class = "btn btn-default button button-medium"]',
    )
