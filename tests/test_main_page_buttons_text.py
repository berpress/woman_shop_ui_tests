"""Test for Main pages button's text"""
import allure

from common.constants import (
    CART_BUTTON_TEXT,
    CONTACT_US_BUTTON_TEXT,
    SIGN_IN_BUTTON_TEXT,
    WOMAN_BUTTON_TEXT,
)


@allure.suite("Главная страница")
@allure.description("Проверка наличия кнопок на главной странице")
@allure.tag("positive", "ST-7")
def test_main_page_buttons_text(app):
    """
    Шаги
    1.Перейти на главную страницу http://automationpractice.com/
    2.Проверить текст кнопки sign in
    3.Проверить текст кнопки Contact us
    4.Проверить текст кнопки Cart
    5.Проверить текст кнопки Women
    """
    app.open_main_page()
    assert app.main_page.cart_button_text() == CART_BUTTON_TEXT
    assert app.main_page.contact_us_text() == CONTACT_US_BUTTON_TEXT
    assert app.main_page.sigh_in_button_text() == SIGN_IN_BUTTON_TEXT
    assert app.main_page.woman_category_text() == WOMAN_BUTTON_TEXT
