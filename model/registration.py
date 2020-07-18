class RegistrationUserData:
    def __init__(
        self,
        email,
        first_name,
        last_name,
        password,
        address,
        city,
        state,
        postal_code,
        country,
        mobile_phone,
        address_alias,
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
