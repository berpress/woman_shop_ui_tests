from locators.goods_page import GoodsPageLocators

class GoodsPage:
    def __init__(self, app):
        self.app = app

    def add_to_wishlist_button(self):
        return self.app.wd.find_element(*GoodsPageLocators.ADD_TO_WISHLIST_BUTTON)

    def close_fancy_box_button(self):
        return self.app.wd.find_element(*GoodsPageLocators.CLOSE_FANCY_BOX)

