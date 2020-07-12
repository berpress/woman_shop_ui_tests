from selenium.webdriver.common.by import By


class MyStorePageLocators:
    MY_WISH_LIST_INPUT_FIELD = (By.ID, "name")
    SAVE_BUTTON = (By.XPATH, "//span[contains(text(),'Save')]")
    NAME_OF_GOOD_WISHLIST = (By.ID, 's_title')