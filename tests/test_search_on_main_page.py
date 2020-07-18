import pytest
import allure
from common.search_on_main_page import NEGATIVE_SEARCH_RESULT


@allure.title("Позитивный тест для поиска на главной странице")
@pytest.mark.parametrize("input_value", ["dress", "shoes", "blouse"])
def test_search_positive(app, input_value):
    """
    Шаги
    1. Открываем главную страницу
    2. Вводим значение input_value в поисковую строку
    3. Нажимаем Enter
    4. Проверяем наличие input_value на странице поиска
    """
    app.open_main_page()
    app.main_page.search(input_value)
    assert (
        app.main_page.positive_search_result() == f'"{input_value.upper()}"'
    ), "Значение input_value не отображается на странице"


@pytest.mark.parametrize("input_value", ["123", "-1", "zxczxc"])
def test_search_negative(app, input_value):
    """
    Шаги
    1. Открываем главную страницу
    2. Вводим значение input_value в поисковую строку
    3. Нажимаем Enter
    4. Проверяем наличие строки No results were found for your search "input_value"
    """
    app.open_main_page()
    app.main_page.search(input_value)
    assert (
        app.main_page.negative_search_result()
        == f'{NEGATIVE_SEARCH_RESULT} "{input_value}"'
    ), "Строка No results were found for your search не найдена"
