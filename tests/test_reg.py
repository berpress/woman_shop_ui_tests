import allure
import faker

from model.registration import RegistrationUserData


fake = faker.Faker()


@allure.suite("Регистрация")
@allure.description("Проверка регистрации с валидными данными")
@allure.tag("positive", "ST-14")
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
    user_data = RegistrationUserData(
        email=fake.email(),
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
    app.login.logout_if_logged_in()
    app.registration.start_registration_process(user_data)
    app.registration.fill_requireds(user_data)
    assert app.registration.check_my_account(), "Регистрация не удалась"
    app.login.logout_if_logged_in()


@allure.suite("Регистрация")
@allure.description("Проверка регистрации с валидными данными и пустым полем имени")
@allure.tag("negative", "ST-14")
def test_registration_negative(app):
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
    user_data = RegistrationUserData(
        email=fake.email(),
        first_name=None,
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
    app.login.logout_if_logged_in()
    app.registration.start_registration_process(user_data)
    app.registration.fill_requireds(user_data)
    assert (
        not app.registration.check_my_account()
    ), "Регистрация не должна была получиться, однако получилась"
    app.login.logout_if_logged_in()
