
def test_email_subscribe(app):
    """
    Steps
    """
    app.open_main_page()
    app.newsletter.input_email(email='orch2id11333@gmail.com')
    app.newsletter.submit_subscribe()
    assert app.newsletter.check_exists_by_class_name('alert alert-success') == 0, \
        'Элемент не был найден на странице'


