from selenium.webdriver.common.by import By


class GoodsPageLocators:
    ADD_TO_WISHLIST_BUTTON = (By.ID, 'wishlist_button')
    CLOSE_FANCY_BOX = (By.XPATH, "//a[@class='fancybox-item fancybox-close']")
    QUANTITY_FIELD = (By.XPATH, "//input[@id='quantity_wanted']")
    QUANTITY_PLUS_BUTTON = (By.XPATH, "//i[@class='icon-plus']")
    QUANTITY_MINUS_BUTTON = (By.XPATH, "//i[@class='icon-minus']")
    ADD_TO_CART = (By.XPATH, "//span[contains(text(),'Add to cart')]")
    SUCCESSFULL_ADD_TO_CART = (By.XPATH, "//h2[contains(.,'Product successfully added to your shopping cart' )]")
    CLOSE_POP_UP = (By.XPATH, "//span[@class='cross']")
    NUMBER_IN_CART = (By.XPATH, "//span[@class='ajax_cart_quantity']")
