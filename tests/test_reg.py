import pytest
from model.registration_model import RegistrationUserData


def test_registration_positive(app):
    """
    Шаги
    1. Открываем главную страницу
    1.1 Разлогин, если залогинены
    2. Нажимаем кнопку 'Sign In'
    3. Вводим валидный емейл
    4. Нажимаем кнопку "Create an account"
    5. Проверяем, что перешли на страницу регистрации аккаунта
    6. Вводим обязательные к заполнению данные
    7. Нажимаем кнопку "Register"
    8. Проверяем, что оказались в личном кабинете
    """
    user_data = RegistrationUserData().random_user()
    app.open_main_page()
    app.login.logout_if_logged_in()
    app.registration.start_registration_process(user_data)
    app.registration.fill_requireds(user_data)
    assert app.registration.check_my_account(), "Регистрация не удалась"
    app.login.logout_if_logged_in()


@pytest.mark.parametrize("fields", [("last_name", "state")])
def test_registration_negative(app, fields):
    """
    Шаги
    1. Открываем главную страницу
    1.1 Разлогин, если залогинены
    2. Нажимаем кнопку 'Sign In'
    3. Вводим валидный емейл
    4. Нажимаем кнопку "Create an account"
    5. Проверяем, что перешли на страницу регистрации аккаунта
    6. Вводим обязательные к заполнению данные, кроме имени
    7. Нажимаем кнопку "Register"
    8. Проверяем, что не оказались в личном кабинете
    """
    user_data = RegistrationUserData().random_user()
    for field in fields:
        setattr(user_data, field, None)
    app.open_main_page()
    app.login.logout_if_logged_in()
    app.registration.start_registration_process(user_data)
    app.registration.fill_requireds(user_data)
    assert (
        not app.registration.check_my_account()
    ), "Регистрация не должна была получиться, однако получилась"
    app.login.logout_if_logged_in()
