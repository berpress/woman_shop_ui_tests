import faker


class ContactUsUserData:
    def __init__(self, email: str, text: str, text_in_form: str):
        self.email = email
        self.text = text
        self.text_in_form = text_in_form

    @staticmethod
    def random_user_data():
        """Функция генерации фейковых данных."""
        fake = faker.Faker()
        return ContactUsUserData(
            email=fake.email(), text=fake.text(), text_in_form=fake.text()
        )
