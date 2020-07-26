import allure
import pytest


@pytest.mark.xfail
@allure.title("Проверка чекбоксов категорий")
@pytest.mark.parametrize("categories,size,color", [("Tops", "S", "White")])
def test_categories_filters(app, categories, size, color):
    """
    Шаги:
    1.Открытие главной страницы
    2.Переход на страницу woman category
    3.Проставление чекбоксов на фильтры
    """
    app.open_main_page()
    app.open_woman_category_page()
    app.woman_category.set_filters(categories, size, color)
    assert app.woman_category.check_filter_result(categories, size, color)
