from locators.my_account import MyAccountPageLocators


class My_Account_page:
    def __init__(self, app):
        self.app = app

    def my_wishlist_button(self):
        return self.app.wd.find_element(*MyAccountPageLocators.MY_WISH_LIST_BUTTON)

    def click_on_my_wishlist_button(self):
        self.my_wishlist_button().click()
