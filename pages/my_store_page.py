from locators.my_store import MyStorePageLocators


class MyStorePage:
    def __init__(self, app):
        self.app = app

    def wish_list_input_field(self):
        return self.app.wd.find_element(*MyStorePageLocators.MY_WISH_LIST_INPUT_FIELD)

    def save_button(self):
        return self.app.wd.find_element(*MyStorePageLocators.SAVE_BUTTON)

    def choose_wishlist(self):
        return self.app.wd.find_element(*MyStorePageLocators.CHOOSE_WISHLIST_BUTTON)

    def name_of_good_wishlist(self):
        return self.app.wd.find_element(*MyStorePageLocators.NAME_OF_GOOD_WISHLIST)

    def send_keys_to_wishlist_input_field(self, text):
        return self.wish_list_input_field().send_keys(text)

    def click_on_save_button(self):
        return self.save_button().click()

    def click_on_choose_wishlist(self):
        return self.choose_wishlist().click()
