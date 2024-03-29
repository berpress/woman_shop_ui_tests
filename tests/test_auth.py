import allure
from pytest_testrail.plugin import testrail

from common.login_constants import AutorizedUser
from model.login import UserData


@allure.suite("Авторизация")
@allure.description("Авторизация с валидными данными")
@allure.tag("positive", "ST-4")
@testrail('C1')
def test_auth_shop(app):
    """
    Шаги
    1. Открываем главную страницу
    2. Нажимаем кнопку логин
    3. Вводим вводим валидные данные
    4. Проверяем данные авторизации
    """
    app.open_main_page()
    user_data = UserData(login="test1910md@mail.ru", password="191089")
    app.login.auth(user_data)
    assert app.login.login_button_get_text() == AutorizedUser.AUTH_USER


@allure.suite("Авторизация")
@allure.description("Проверка авторизации с пустым полем логина")
@allure.tag("positive", "ST-4")
def test_empty_email_auth(app):
    """
    Шаги
    1. Открываем главную страницу
    2. Нажимаем кнопку логин
    3. Вводим вводим пустой логин
    4. Проверяем данные авторизации
    """
    app.open_main_page()
    user_data = UserData(login=None, password="191089")
    app.login.auth(user_data)
    assert app.login.login_auth_alert_get_text() == AutorizedUser.AUTH_EMAIL_ALERT_TEXT


@allure.suite("Авторизация")
@allure.description("Проверка авторизации с пустым полем пароля")
@allure.tag("positive", "ST-4")
def test_empty_password_auth(app):
    """
    Шаги
    1. Открываем главную страницу
    2. Нажимаем кнопку логин
    3. Вводим вводим пустой пароль
    4. Проверяем данные авторизации
    """
    app.open_main_page()
    user_data = UserData(login="test1910md@mail.ru", password=None)
    app.login.auth(user_data)
    assert (
        app.login.login_auth_alert_get_text()
        == AutorizedUser.AUTH_PASS_ALERT_TEXT_EMPTY_PASSWORD
    )


@allure.suite("Авторизация")
@allure.description("Проверка авторизации с некорректным емейлом")
@allure.tag("positive", "ST-4")
def test_incorrect_email_auth(app):
    """
    Шаги
    1. Открываем главную страницу
    2. Нажимаем кнопку логин
    3. Вводим вводим некорректную почту
    4. Проверяем данные авторизации
    """
    app.open_main_page()
    user_data = UserData(login="5555", password="191089")
    app.login.auth(user_data)
    assert (
        app.login.login_auth_alert_get_text()
        == AutorizedUser.AUTH_INVALID_EMAIL_ALERT_TEXT
    )


@allure.suite("Авторизация")
@allure.description("Проверка авторизации с некорректным паролем")
@allure.tag("positive", "ST-4")
def test_incorrect_pass_auth(app):
    """
    Шаги
    1. Открываем главную страницу
    2. Нажимаем кнопку логин
    3. Вводим вводим некорректный пароль
    4. Проверяем данные авторизации
    """
    app.open_main_page()
    user_data = UserData(login="test1910md@mail.ru", password="111")
    app.login.auth(user_data)
    assert (
        app.login.login_auth_alert_get_text()
        == AutorizedUser.AUTH_INVALID_PASS_ALERT_TEXT
    )
