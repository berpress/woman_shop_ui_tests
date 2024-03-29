import allure

from model.login import UserData


@allure.suite("Вишлист")
@allure.description("Проверка поиска с валидными данными")
@allure.tag("positive", "ST-19")
def test_wishlist(app):
    """
       Шаги
       1. Открываем главную страницу
       2. Авторизовываемся
       3. Кликаем на кнопку My Wishlist
       4. Вводим название нового вишлиста
       5. Нажимаем 'Save'
       6. Открываем главную страницу
       7. Кликаем на товар " Black Blouse"
       8. Кликаеи "Add to wishlist"
       9. Закрываем модальное окно
       10. Переходим на страницу My wishlist
       11. Кликаем на созданный вишллист - "Test wishlist"
       12. Проверяем налчие черной блузы внутри вишлиста
       """
    app.open_main_page()
    user_data = UserData(login="pestot@mail.ru", password="221052")
    app.login.auth(user_data)
    app.my_account.click_on_my_wishlist_button()
    app.my_store.send_keys_to_wishlist_input_field("Test wishlist")
    app.my_store.click_on_save_button()
    assert "Test wishlist" in app.my_store.choose_wishlist().text
    app.open_main_page()
    app.main_page.click_on_girl_in_black()
    app.goods_page.click_on_add_to_wishlist()
    app.goods_page.close_fancy_box_button()
    app.open_wishlist()
    app.my_store.click_on_choose_wishlist()
    assert "Blouse" in app.my_store.name_of_good_wishlist().text
