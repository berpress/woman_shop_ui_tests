"""Order page locators."""

from selenium.webdriver.common.by import By


class OrderPageLocators:
    SUMMARY_PROCEED_TO_CHECKOUT_BUTTON = (
        By.XPATH,
        '//a[@class = "button btn btn-default standard-checkout button-medium"]',
    )
    ADDRESS_PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, '//button[@name= "processAddress"]')
    SHIPPING_PROCEED_TO_CHECKOUT_BUTTON = (
        By.XPATH,
        '//button[@name= "processCarrier"]',
    )
    TERMS_OF_SERVICE_CHECKBOX = (By.XPATH, '//div[@class= "checker"]')
    PAY_BY_BANK_WIRE_BUTTON = (
        By.XPATH,
        '//p[@class = "payment_module"]/a[@class = "bankwire"]',
    )
    PAY_BY_CHECK_BUTTON = (
        By.XPATH,
        '//p[@class = "payment_module"]/a[@class = "cheque"]',
    )
    CONFIRM_ORDER_BUTTON = (
        By.XPATH,
        '//button[@class="button btn btn-default button-medium"]',
    )
    ORDER_CREATED_TEXT_BY_CARD = (
        By.XPATH,
        '//div[@class="box"]//strong[@class="dark"]',
    )
    ORDER_CREATED_TEXT_BY_CHEQUE = (By.XPATH, '//*[@class="alert alert-success"]')
    ORDER_INFO_BY_CARD = (By.XPATH, '//div[@class="box"]')
    ORDER_INFO_BY_CHEQUE = (By.XPATH, '//div[@class="box order-confirmation"]')
    TERMS_OF_SERVICE_AGREEMENT = (By.XPATH, '//*[@class="fancybox-error"]')
    COMMENT_FIELD = (By.XPATH, '//*[@class="form-control"]')
