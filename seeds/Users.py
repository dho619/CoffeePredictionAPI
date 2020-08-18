from flask_seeder import Seeder, Faker, generator
from werkzeug.security import generate_password_hash
import random, string

from app.models.Users import Users


# SQLAlchemy database model
class User(Users):
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return "Name=%s, Email=%s, Password=%s" % (self.name, self.email, self.password)

#Seeder Users
class UserSeeder(Seeder):

  # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects

        faker = Faker(
            cls=User,
            init={
                "name": generator.Name(),
                "email": generator.Name(),#nao consigo criar com email
                "password": generate_password_hash('123')
            }
        )

        # Create 5 users
        for user in faker.create(5):
            print("Adding user: %s" % user)
            self.db.session.add(user)
