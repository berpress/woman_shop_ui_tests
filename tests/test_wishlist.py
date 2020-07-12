import time

from model.login import UserData


def test_wishlist(app):
    app.open_main_page()
    user_data = UserData(login='pestot@mail.ru', password='221052')
    app.login.auth(user_data)
    app.my_account.my_wishlist_button().click()
    app.my_store.wish_list_input_field().send_keys('Test wishlist')
    app.my_store.save_button().click()
    assert 'Test wishlist' in app.wd.page_source
    app.open_main_page()
    app.main_page.girl_in_black().click()
    app.goods_page.add_to_wishlist_button().click()
    app.goods_page.close_fancy_box_button().click()
    app.open_wishlist()
    app.my_store.choose_wishlist().click()
    assert 'Blouse' in app.my_store.name_of_good_wishlist().text
