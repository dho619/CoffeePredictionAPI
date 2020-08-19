from flask_seeder import Seeder, Faker, generator
import random, string

from app.models.Areas import Areas

class Area(Areas):
    def __init__(self, name, description, location, type_area_id, user_id):
        self.name = name
        self.description = description
        self.location = location
        self.type_area_id = type_area_id
        self.user_id = user_id

    def __str__(self):
        return "Name=%s, Description=%s, Location=%s" % (self.name, self.description, self.location)

#Seeder Areas
class AreaSeeder(Seeder):

  # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create Area objects
        faker = Faker(
            cls=Area,
            init={
                "name": generator.Name(),
                "description": generator.Name(),
                "location": generator.Integer(start=2000, end=10000),
                "type_area_id": generator.Integer(start=1, end=3),
                "user_id": 2
            }
        )

        # Create 5 users
        for area in faker.create(10):
            print("Adding area: %s" % area)
            self.db.session.add(area)
