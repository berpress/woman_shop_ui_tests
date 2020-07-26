import allure

from common.contact_us_constants import ContactUs
from model.contact_us import ContactUsUserData
from pages.application import logger


@allure.suite("Обратная связь")
@allure.description("Отправка сообщения CUSTOMER SERVICE с заполнением валидных данных")
@allure.tag("positive", "ST-29")
def test_contact_us_field(app):
    """
    1. Открывает главную страницу
    2. Нажимаем на кнопку Contact us
    3. Кликаем на Subject Heading
    4. Вводим email адрес
    5. Вводим в значение в поле Order reference
    6. Прикладываем файл --в данный момент не работает
    7. Вводим сообщение в Message
    8. Кликаем на кнопку Send.
    """
    user_data = ContactUsUserData(
        email="orchid345617@gmail.com",
        text="Text in order reference",
        text_in_form="Text in message field",
    )
    app.open_main_page()
    app.contact_us.find_and_click_contact_us_button()
    app.contact_us.click_on_subject_heading_button()
    # app.contact_us.click_on_choose_file(create_tmp_file())
    app.contact_us.fill_data(user_data)
    app.contact_us.click_in_send_button()
    assert app.contact_us.get_text_from_success_alert() == ContactUs.SUCCESS_ALERT


@allure.suite("Обратная связь")
@allure.description("Отправка сообщения CUSTOMER SERVICE без выбора Subject Heading")
@allure.tag("negative", "ST-29")
def test_contact_us_with_empty_subject_heading(app):
    """
    1. Открывает главную страницу
    2. Нажимаем на кнопку Contact us
    3. Отславяем пустым Subject Heading
    4. Вводим email адрес
    5. Вводим в значение в поле Order reference
    6. Прикладываем файл --в данный момент не работает
    7. Вводим сообщение в Message
    8. Кликаем на кнопку Send.
    """
    user_data = ContactUsUserData(
        email="orchid345617@gmail.com",
        text="Text in order reference",
        text_in_form="Text in message field",
    )
    app.open_main_page()
    logger.info("Началось выполнение теста")
    app.contact_us.find_and_click_contact_us_button()
    # app.contact_us.click_on_choose_file(create_tmp_file())
    app.contact_us.fill_data(user_data)
    app.contact_us.click_in_send_button()
    assert (
        app.contact_us.get_text_from_alert_with_error()
        == ContactUs.EMPTY_SUBJECT_HEADING_ALERT
    )
    logger.info("Тест успешно завершился")


@allure.suite("Обратная связь")
@allure.description("Отправка сообщения CUSTOMER SERVICE с пустыми полем емейла")
@allure.tag("negative", "ST-29")
def test_contact_us_with_empty_email(app):
    """
    1. Открывает главную страницу
    2. Нажимаем на кнопку Contact us
    3. Выбираем Subject Heading
    4. Оставляем поле email пустым
    5. Вводим в значение в поле Order reference
    6. Прикладываем файл --в данный момент не работает
    7. Вводим сообщение в Message
    8. Кликаем на кнопку Send.
    """
    user_data = ContactUsUserData(
        email=None, text="Text in order reference", text_in_form="Text in message field"
    )
    app.open_main_page()
    logger.info("Началось выполнение теста")
    app.contact_us.find_and_click_contact_us_button()
    app.contact_us.click_on_subject_heading_button()
    # app.contact_us.click_on_choose_file(create_tmp_file())
    app.contact_us.fill_data(user_data)
    app.contact_us.click_in_send_button()
    assert (
        app.contact_us.get_text_from_alert_with_error() == ContactUs.EMPTY_EMAIL_ALERT
    )
    logger.info("Тест успешно завершился")


@allure.suite("Обратная связь")
@allure.description("Отправка сообщения CUSTOMER SERVICE с пустыми сообщением")
@allure.tag("negative", "ST-29")
def test_contact_us_with_empty_message(app):
    """
    1. Открывает главную страницу
    2. Нажимаем на кнопку Contact us
    3. Выбираем Subject Heading
    4. Вводим email
    5. Вводим в значение в поле Order reference
    6. Прикладываем файл --в данный момент не работает
    7. Ничего не вводим в поле Message
    8. Кликаем на кнопку Send.
    """
    user_data = ContactUsUserData(
        email="orchid345617@gmail.com",
        text="Text in order reference",
        text_in_form=None,
    )
    app.open_main_page()
    logger.info("Началось выполнение теста")
    app.contact_us.find_and_click_contact_us_button()
    app.contact_us.click_on_subject_heading_button()
    # app.contact_us.click_on_choose_file(create_tmp_file())
    app.contact_us.fill_data(user_data)
    app.contact_us.click_in_send_button()
    assert (
        app.contact_us.get_text_from_alert_with_error() == ContactUs.EMPTY_MESSAGE_ALERT
    )
    logger.info("Тест успешно завершился")
