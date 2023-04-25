from models import Users, History
from faker import Faker
import random

fake = Faker()

for i in range(20):
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    Users.createUser(username=username, email=email, pswd=password)

# Get all users
users = Users.getAllUsers()

# Add 200 fake games
for i in range(200):
    appleid = random.choice(users)['id']
    yargid = random.choice(users)['id']
    applescore = 4 if random.randint(1,2)==2 else random.randint(1,3)
    yargscore = 4 if applescore<4 else random.randint(1,3)
    History.append(appleid, yargid, applescore, yargscore)
