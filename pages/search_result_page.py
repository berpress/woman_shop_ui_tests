from locators.search_result_page import SearchResultPageLocators


class SearchResultPage:
    def __init__(self, app):
        self.app = app

    def more_button(self):
        return self.app.wd.find_element(*SearchResultPageLocators.MORE_BUTTON)

    def result_good(self):
        return self.app.wd.find_element(*SearchResultPageLocators.RESULT_GOOD)

    def move_to_result_button(self):
        return self.app.ac.move_to_element(self.result_good()).perform()

    def click_on_more_button(self):
        return self.app.ac.move_to_element(self.more_button()).click().perform()

    def more_button_is_displayed(self):
        return self.more_button().is_displayed()
