from model.registration import RegistrationUserData
import pytest


@pytest.mark.skip
def test_registration(app):
    """
    Шаги
    1. Открываем главную страницу
    2. Нажимаем кнопку 'Sign In'
    3. Вводим валидный емейл
    4. Нажимаем кнопку "Create an account"
    5. Проверяем, что перешли на страницу регистрации аккаунта
    6. Вводим обязательные к заполнению данные
    7. Нажимаем кнопку "Register"
    8. Проверяем, что оказались в личном кабинете
    """
    user_data = RegistrationUserData(
        email="test@email.inno",
        first_name="Vlad",
        last_name="Lubomski",
        password="123456",
        address="Sverdlova str.",
        city="Togliatty",
        state="63",
        postal_code="44036",
        country="Russia",
        mobile_phone="88008008080",
        address_alias="tlt",
    )
    app.open_main_page()
    app.registration.start_registration_process(user_data)
    app.registration.fill_requireds(user_data)
    assert app.registration.check_my_account() is True, "Регистрация не удалась"
