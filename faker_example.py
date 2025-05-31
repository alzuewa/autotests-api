from faker import Faker


fake = Faker('de_DE')

print(fake.name())
print(fake.address())
print(fake.email())

data = {
    'email': fake.email(),
    'name': fake.name(),
    'age': fake.random_int(min=18, max=100)
}
print(data)