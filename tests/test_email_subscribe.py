import faker


def test_valid_email(app):
    """
    Шаги:
    1. Открывается главная страница
    2. Вводим валидный email и делаем тап на кнопку ">"
    3. Проверяем наличие элемента на странице
    """
    app.open_main_page()
    fake = faker.Faker()
    login = fake.email()
    app.newsletter.email_subscribe(login)
    assert app.newsletter.check_success_alert(), "Элемент не был найден."


def test_invalid_email(app):
    """
    Шаги:
    1. Открывается главная страница
    2. Вводим невалидный email и делаем тап на кнопку ">"
    3. Проверяем наличие элемента на странице
    """
    app.open_main_page()
    fake = faker.Faker()
    login = fake.name()
    app.newsletter.email_subscribe(login)
    assert app.newsletter.check_unsuccessful_alert(), "Элемент не был найден."


def test_already_used_email(app):
    """
    Шаги:
    1. Открывается главная страница
    2. Вводим уже использованный  email и делаем тап на кнопку ">"
    3. Проверяем наличие элемента на странице
    """
    app.open_main_page()
    app.newsletter.email_subscribe(email='orchid345617@gmail.com')
    assert app.newsletter.check_unsuccessful_alert(), "Элемент не был найден."


def test_empty_email(app):
    """
    Шаги:
    1. Открывается главная страница
    2. Ничего не вводим и делаем тап на кнопку ">"
    3. Проверяем наличие элемента на странице
    """
    app.open_main_page()
    app.newsletter.email_subscribe(email=' ')
    assert app.newsletter.check_unsuccessful_alert(), "Элемент не был найден."
