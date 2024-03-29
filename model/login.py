import faker


class UserData:
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    @staticmethod
    def random_user():
        """Функция генерации фейковых данных."""
        fake = faker.Faker()
        return UserData(login=fake.email(), password=fake.password())
