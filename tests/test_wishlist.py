import time

from model.login import UserData


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
    user_data = UserData(login='pestot@mail.ru', password='221052')
    app.login.auth(user_data)
    app.click_on_locator(app.my_account.my_wishlist_button())
    app.send_keys_to_locator(app.my_store.wish_list_input_field(), 'Test wishlist')
    app.click_on_locator(app.my_store.save_button())
    assert 'Test wishlist' in app.my_store.choose_wishlist().text
    app.open_main_page()
    app.click_on_locator(app.main_page.girl_in_black())
    app.click_on_locator(app.goods_page.add_to_wishlist_button())
    app.click_on_locator(app.goods_page.close_fancy_box_button())
    app.open_wishlist()
    app.click_on_locator(app.my_store.choose_wishlist())
    assert 'Blouse' in app.my_store.name_of_good_wishlist().text
