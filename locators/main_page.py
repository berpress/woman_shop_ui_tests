from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.ID, 'search_query_top')
    SEARCH_RESULT = (By.XPATH, '//span[@class="heading-counter"]')
