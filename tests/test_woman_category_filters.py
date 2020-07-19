import allure
import pytest


@pytest.mark.xfail
@allure.title("Проверка чекбоксов категорий")
@pytest.mark.parametrize(
    "categories,size,colors", [("Tops", "S", "White"), ("Dress", "M", "Orange")]
)
def test_categories_filters(app, categories, size, colors):
    """
    Шаги:
    1.Открытие главной страницы
    2.Переход на страницу woman category
    3.Проставление чекбоксов на фильтры
    """
    app.open_main_page()
    app.open_woman_category_page()
    app.woman_category.make_filters(categories, size, colors)
    assert app.woman_category.check_result(categories, size, colors)
