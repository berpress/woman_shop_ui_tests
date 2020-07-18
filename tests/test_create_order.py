from common.order_page import ORDER_CREATED_SUCCESS


def test_create_new_order(login):
    """
    Шаги:
    1.Авторизация
    2.Переход на главную страницу
    3.Наведение мышкой на первый товар на главной странице
    4.Добавление товара в корзину
    5.Переход к оформлению заказа
    6.Нажатие кнопки proceed_to_checkout на шаге summary
    7.Нажатие кнопки proceed_to_checkout на шаге address
    8.Проставление чекбокса terms of service
    9.Выбор способа оплаты by_bank_wire
    10.Подтверждение заказа
    11.Переход на страницу истории заказов
    :param login:
    """
    login.open_main_page()
    login.main_page.focus_first_good()
    login.main_page.add_to_cart_button()
    login.main_page.proceed_to_checkout_button()
    login.order_page.summary_proceed_to_checkout()
    login.order_page.address_proceed_to_checkout()
    login.order_page.terms_checkbox_click()
    login.order_page.shipping_proceed_to_checkout()
    login.order_page.pay_by_bank_wire()
    login.order_page.confirm_order()
    assert login.order_page.order_created() == ORDER_CREATED_SUCCESS
    code = login.order_page.order_code()
    login.open_order_history_page()
    assert code in login.get_page_source()
