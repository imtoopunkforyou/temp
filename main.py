from faker import Faker
fake = Faker()

name = fake.name()
# 'Lucy Cechtelar'

addr = fake.address()
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

print('*'*10)
print(
    name, addr
)

print('*'*10)
