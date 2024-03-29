import allure

from locators.woman_category_page import WomanCategoryPageLocators


class WomanCategoryPage:
    def __init__(self, app):
        self.app = app
        self.categories_dict = {"top": self.top_checkbox, "dress": self.dress_checkbox}
        self.size_dict = {
            "s": self.s_size_checkbox,
            "m": self.m_size_checkbox,
            "l": self.l_size_checkbox,
        }
        self.color_dict = {
            "beige": self.beige_color_button,
            "white": self.white_color_button,
            "black": self.black_color_button,
            "orange": self.orange_color_button,
            "blue": self.blue_color_button,
            "green": self.green_color_button,
            "yellow": self.yellow_color_button,
            "pink": self.pink_color_button,
        }

    @allure.step("Проставление чекбокса top на странице woman category")
    def top_checkbox(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.TOPS_CHECKBOX
        ).click()

    @allure.step("Проставление чекбокса dress на странице woman category")
    def dress_checkbox(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.DRESS_CHECKBOX
        ).click()

    def top_checkbox_is_selected(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.TOPS_CHECKBOX
        ).is_selected()

    def dress_checkbox_is_selected(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.DRESS_CHECKBOX
        ).is_selected()

    @allure.step("Проставление чекбокса S size на странице woman category")
    def s_size_checkbox(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.S_SIZE_CHECKBOX
        ).click()

    @allure.step("Проставление чекбокса M size на странице woman category")
    def m_size_checkbox(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.M_SIZE_CHECKBOX
        ).click()

    @allure.step("Проставление чекбокса L size на странице woman category")
    def l_size_checkbox(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.M_SIZE_CHECKBOX
        ).click()

    @allure.step("Нажатие кнопки beige color на странице woman category")
    def beige_color_button(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.BEIGE_COLOR_BUTTON
        ).click()

    @allure.step("Нажатие кнопки white color на странице woman category")
    def white_color_button(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.WHITE_COLOR_BUTTON
        ).click()

    @allure.step("Нажатие кнопки black color на странице woman category")
    def black_color_button(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.BLACK_COLOR_BUTTON
        ).click()

    @allure.step("Нажатие кнопки orange color на странице woman category")
    def orange_color_button(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.ORANGE_COLOR_BUTTON
        ).click()

    @allure.step("Нажатие кнопки blue color на странице woman category")
    def blue_color_button(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.BLUE_COLOR_BUTTON
        ).click()

    @allure.step("Нажатие кнопки green color на странице woman category")
    def green_color_button(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.GREEN_COLOR_BUTTON
        ).click()

    @allure.step("Нажатие кнопки yellow color на странице woman category")
    def yellow_color_button(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.YELLOW_COLOR_BUTTON
        ).click()

    @allure.step("Нажатие кнопки pink color на странице woman category")
    def pink_color_button(self):
        return self.app.wd.find_element(
            *WomanCategoryPageLocators.PINK_COLOR_BUTTON
        ).click()

    @allure.step("Установка фильтров")
    def set_filters(self, categories: str, size: str, color: str):
        return (
            self.categories_dict[categories],
            self.size_dict[size],
            self.color_dict[color],
        )

    def check_filter_result(self, categories: str, size: str, color: str):
        pass
