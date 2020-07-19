from common.ContactUs_Constants import ContactUs


def test_contact_us_field(app):
    """
    1. Открывает главную страницу
    2. Нажимаем на кнопку Contact us
    3. Кликаем на Subject Heading
    4. Вводим email адрес
    5. Вводим в значение в поле Order reference
    6. Прикладываем файл --в данный момент не работает
    7. Вводим сообщение в Message
    8. Кликаем на кнопку Send

    """
    app.open_main_page()
    app.contact_us.find_and_click_contact_us_button()
    app.contact_us.click_on_subject_heading_button()
    app.contact_us.click_on_email_field(email="orchid3456176@gmail.com")
    app.contact_us.click_on_order_reference_field(text="Text in order reference")
    # app.contact_us.click_on_choose_file(create_tmp_file())
    app.contact_us.input_message_text(text="Text in message field")
    app.contact_us.click_in_send_button()
    assert app.contact_us.get_text_from_success_alert() == ContactUs.SUCCESS_ALERT


def test_contact_us_with_empty_subject_heading(app):
    """
    1. Открывает главную страницу
    2. Нажимаем на кнопку Contact us
    3. Отславяем пустым Subject Heading
    4. Вводим email адрес
    5. Вводим в значение в поле Order reference
    6. Прикладываем файл --в данный момент не работает
    7. Вводим сообщение в Message
    8. Кликаем на кнопку Send

    """
    app.open_main_page()
    app.contact_us.find_and_click_contact_us_button()
    app.contact_us.click_on_email_field(email="orchid3456176@gmail.com")
    app.contact_us.click_on_order_reference_field(text="Text in order reference")
    # app.contact_us.click_on_choose_file(create_tmp_file())
    app.contact_us.input_message_text(text="Text in message field")
    app.contact_us.click_in_send_button()
    assert (
        app.contact_us.get_text_from_alert_with_error()
        == ContactUs.EMPTY_SUBJECT_HEADING_ALERT
    )


def test_contact_us_with_empty_email(app):
    """
    1. Открывает главную страницу
    2. Нажимаем на кнопку Contact us
    3. Выбираем Subject Heading
    4. Оставляем поле email пустым
    5. Вводим в значение в поле Order reference
    6. Прикладываем файл --в данный момент не работает
    7. Вводим сообщение в Message
    8. Кликаем на кнопку Send

    """
    app.open_main_page()
    app.contact_us.find_and_click_contact_us_button()
    app.contact_us.click_on_subject_heading_button()
    app.contact_us.click_on_email_field(email="")
    app.contact_us.click_on_order_reference_field(text="Text in order reference")
    # app.contact_us.click_on_choose_file(create_tmp_file())
    app.contact_us.input_message_text(text="Text in message field")
    app.contact_us.click_in_send_button()
    assert (
        app.contact_us.get_text_from_alert_with_error() == ContactUs.EMPTY_EMAIL_ALERT
    )


def test_contact_us_with_empty_message(app):
    """
    1. Открывает главную страницу
    2. Нажимаем на кнопку Contact us
    3. Выбираем Subject Heading
    4. Вводим email
    5. Вводим в значение в поле Order reference
    6. Прикладываем файл --в данный момент не работает
    7. Ничего не вводим в поле Message
    8. Кликаем на кнопку Send

    """
    app.open_main_page()
    app.contact_us.find_and_click_contact_us_button()
    app.contact_us.click_on_subject_heading_button()
    app.contact_us.click_on_email_field(email="orchid345617@gmail.com")
    app.contact_us.click_on_order_reference_field(text="Text in order reference")
    # app.contact_us.click_on_choose_file(create_tmp_file())
    app.contact_us.input_message_text(text="")
    app.contact_us.click_in_send_button()
    assert (
        app.contact_us.get_text_from_alert_with_error() == ContactUs.EMPTY_MESSAGE_ALERT
    )