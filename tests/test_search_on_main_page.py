import pytest


@pytest.mark.parametrize("input_value", ["123", 'dress'])
def test_search(app, input_value):
    """
    Шаги
    1. Открываем главную страницу
    2. Вводим значение input_value в поисковую строку
    3. Нажимаем Enter
    4. Проверяем наличие строки results have been found
    """
    app.open_main_page()
    app.main_page.search(input_value)
    assert app.main_page.search_result()
