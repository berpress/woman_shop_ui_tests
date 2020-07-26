import time
from common.constants import ADD_TO_CART_BLOUSES_NUMBER, SUCCESS_ADD_TO_CART_TEXT


def test_add_to_cart_from_searching(app):
    """
    Шаги:
    1) Зайти на automation-pratice.com
    2) В поисковой строке ввести названия товара (напр. Blouse)
    3) Сделать тап на кнопку "Найти"
    4) Сделать тап на кноку "More"
    5) Изменить значение в поле "Quantity"
    6) Изменить значение в поле "Size"
    7) Изменить значение в поле Color
    8) Сделать тап на кнопку "Add to card"
    9) Проверить текст на pop-up окне "Product successfully added to your shopping cart"
    10) Закрыть pop-up окно
    11) Убедиться, что на главной странице в поле Cart изменился счетчик
        """
    app.open_main_page()
    app.main_page.search('Blouse')
    app.search_result_page.move_to_result_button()
    assert app.search_result_page.more_button_is_displayed() is True
    app.search_result_page.click_on_more_button()
    app.goods_page.click_on_quantity_field_plus_button()
    app.goods_page.click_on_quantity_field_minus_button()
    app.goods_page.send_keys_to_quantity_filed(ADD_TO_CART_BLOUSES_NUMBER)
    app.goods_page.click_add_to_cart_button()
    text = app.goods_page.text_of_successfull_additional()
    assert text == SUCCESS_ADD_TO_CART_TEXT
    app.goods_page.click_on_close_window_button()
    assert app.goods_page.quantity_in_cart_text() == str(ADD_TO_CART_BLOUSES_NUMBER)

