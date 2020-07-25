from selenium.webdriver.common.by import By


class SearchResultPageLocators:
    MORE_BUTTON = (By.XPATH, "//span[contains(text(),'More')]")
    RESULT_GOOD = (By.XPATH, "//a[@class='product_img_link']//img[@class='replace-2x img-responsive']")
