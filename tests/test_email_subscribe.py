import allure
import pytest

from common.Subscribed_Contants import EmailSubscribe


@allure.suite("Подписка на email рассылку")
@allure.description("Проверка подписки с валидным емейлом")
@allure.tag("positive", "ST-15")
def test_valid_email(app):
    """
    Шаги:
    1. Открывается главная страница
    2. Вводим валидный email и делаем тап на кнопку ">"
    3. Проверяем наличие элемента на странице
    """
    app.open_main_page()
    valid_email = app.newsletter.generate_valid_email()
    app.newsletter.email_subscribe(valid_email)
    assert (
        app.newsletter.email_subscribe_get_text()
        == EmailSubscribe.VALID_EMAIL_ALERT_TEXT
    )


@allure.suite("Подписка на email рассылку")
@allure.description("Проверка подписки с невалидным емейлом")
@allure.tag("negative", "ST-15")
@pytest.mark.parametrize("email_value", ["123", "yandex", "@", " -*&"])
def test_invalid_email(app, email_value):
    """
    Шаги:
    1. Открывается главная страница
    2. Вводим невалидный email и делаем тап на кнопку ">"
    3. Проверяем наличие элемента на странице
    """
    app.open_main_page()
    app.newsletter.email_subscribe(email_value)
    assert (
        app.newsletter.email_subscribe_get_text_with_error()
        == EmailSubscribe.INVALID_EMAIL_ALERT_TEXT
    )


@allure.suite("Подписка на email рассылку")
@allure.description("Проверка подписки с вводом использованного раннее email")
@allure.tag("negative", "ST-15")
def test_already_used_email(app):
    """
    Шаги:
    1. Открывается главная страница
    2. Вводим уже использованный  email и делаем тап на кнопку ">"
    3. Проверяем наличие элемента на странице
    """
    app.open_main_page()
    app.newsletter.email_subscribe(email="orchid345617@gmail.com")
    assert (
        app.newsletter.email_subscribe_get_text_with_error()
        == EmailSubscribe.ALREADY_USED_EMAIL_TEXT
    )


@allure.suite("Подписка на email рассылку")
@allure.description("Проверка подписки с пустым полем email")
@allure.tag("negative", "ST-15")
def test_empty_email(app):
    """
    Шаги:
    1. Открывается главная страница
    2. Ничего не вводим и делаем тап на кнопку ">"
    3. Проверяем наличие элемента на странице
    """
    app.open_main_page()
    app.newsletter.email_subscribe(email=" ")
    assert (
        app.newsletter.email_subscribe_get_text_with_error()
        == EmailSubscribe.EMPTY_EMAIL_ALERT_TEXT
    )
