from selenium.webdriver.common.by import By


class GoodsPageLocators:
    ADD_TO_WISHLIST_BUTTON = (By.ID, 'wishlist_button')
    CLOSE_FANCY_BOX = (By.XPATH, "//a[@class='fancybox-item fancybox-close']")
