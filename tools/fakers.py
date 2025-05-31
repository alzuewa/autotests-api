from faker import Faker


class Fake:

    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        return self.faker.text()

    def uuid4(self) -> str:
        return self.faker.uuid4()

    def email(self) -> str:
        return self.faker.email()

    def sentence(self) -> str:
        return self.faker.sentence()

    def password(self) -> str:
        return self.faker.password()

    def first_name(self) -> str:
        return self.faker.first_name()

    def last_name(self) -> str:
        return self.faker.last_name()

    def middle_name(self) -> str:
        return self.faker.middle_name()

    def estimated_time(self) -> str:
        return f'{self.integer(2, 10)} weeks'

    def integer(self, start: int = 1, end: int = 100) -> int:
        return self.faker.random_int(min=start, max=end)

    def max_score(self) -> int:
        return self.integer(50, 100)

    def min_score(self) -> int:
        return self.integer(1, 30)


fake = Fake(faker=Faker())
fake_en = Fake(faker=Faker('en_US'))
fake_de = Fake(faker=Faker('de_DE'))
