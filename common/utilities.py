def fill_input(element, value):
    """Заполняет поле в зависимости от его типа и передаваемого значения"""
    if value:
        element().send_keys(value)
