import faker


def test_email_subscribe(app):
    """
    Шаги:
    1. Открывается главная страница
    2. Вводим email и делаем тап на кнопку ">"
    3. Проверяем наличие элемента на странице
    """
    app.open_main_page()
    fake = faker.Faker()
    login = fake.email()
    app.newsletter.input_email_and_submit_subscribe(login)
    assert app.newsletter.check_success_alert(), "Элемент не был найден."
