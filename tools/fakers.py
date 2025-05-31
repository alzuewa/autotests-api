from faker import Faker


class Fake:
    """
    Generates random test data using Faker library
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Faker() instance used for data generating
        """
        self.faker = faker

    def text(self) -> str:
        """
        Generates random text
        :return: random text
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Generates random UUID4
        :return: random UUID4
        """
        return self.faker.uuid4()

    def email(self) -> str:
        """
        Generates random email
        :return:  random email
        """
        return self.faker.email()

    def sentence(self) -> str:
        """
        Generates random sentence
        :return: random sentence
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Generates random password
        :return: random password
        """
        return self.faker.password()

    def first_name(self) -> str:
        """
        Generates random first name
        :return: random first name
        """
        return self.faker.first_name()

    def last_name(self) -> str:
        """
        Generates random last name
        :return: random last name
        """
        return self.faker.last_name()

    def middle_name(self) -> str:
        """
        Generates random middle name
        :return: random middle name
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Generates string with time estimate assumption (for instance, `2 weeks`)
        :return: string with generated estimated time
        """
        return f'{self.integer(2, 10)} weeks'

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Generates random integer within a given range
        :param start: range start (inclusive)
        :param end: range end (inclusive)
        :return: random integer
        """
        return self.faker.random_int(min=start, max=end)

    def max_score(self) -> int:
        """
        Generates random maximum score within a range of 50 and 100
        :return: random score
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Generates random minimum score within a range of 1 and 30
        :return: random score
        """
        return self.integer(1, 30)


fake = Fake(faker=Faker())
fake_en = Fake(faker=Faker('en_US'))
fake_de = Fake(faker=Faker('de_DE'))
