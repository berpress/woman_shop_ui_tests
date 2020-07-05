


def test_text(app):
    """
    Шаги
    1.Перейти на главную страницу http://automationpractice.com/
    2.Проверить текст кнопки sign in
    3.Проверить текст кнопки Contact us
    4.Проверить текст кнопки Cart
    5.Проверить текст кнопки Women
    """
    app.open_main_page()
    assert app.main_page.cart_button_text() == "Cart (empty)"
    assert app.main_page.contact_us_text() == "Contact us"
    assert app.main_page.sigh_in_button_text() == "Sign in"
    assert app.main_page.woman_category_text() == 'WOMEN'
