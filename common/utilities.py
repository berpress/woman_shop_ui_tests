def fill_input(element, value):
    """Заполняет поле в зависимости от его типа и передаваемого значения"""
    if value:
        element().send_keys(value)


def fill_select(element, value):
    """Выбирает селект, если было передано значение value."""
    if value:
        element().click()
