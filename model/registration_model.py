from faker import Faker


class RegistrationUserData:
    def __init__(
        self,
        email=None,
        first_name=None,
        last_name=None,
        password=None,
        address=None,
        city=None,
        state=None,
        postal_code=None,
        country=None,
        mobile_phone=None,
        address_alias=None,
    ):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.mobile_phone = mobile_phone
        self.address_alias = address_alias

    @staticmethod
    def random_user():
        fake = Faker()
        return RegistrationUserData(
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            password=fake.password(),
            address=fake.street_address(),
            city=fake.city(),
            state=fake.state(),
            postal_code=fake.random_int(40000, 50000),
            country=fake.country(),
            mobile_phone=fake.msisdn(),
            address_alias=fake.word(),
        )
