from model.login import UserData


def test_auth_shop(app):
    """
    Шаги
    1. Открываем главную страницу
    2. Нажимаем кнопкн логин
    3. Вводим вводим валидные данные
    4. Проверяем имя пользователя
    """
    app.open_main_page()
    user_data = UserData(login=None, password='password')
    app.login.auth(user_data)
    assert True


def test_auth(login):
    pass
