#!/usr/bin/python3

import unittest
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.country import Country

class TestModels(unittest.TestCase):
    def test_user(self):
        user = User(email="db@email.com", password="123456789")
        self.assertEqual(user.email, "db@email.com")
        self.assertEqual(user.password, "123456789")

    def test_place(self):
        user = User(email="aze@email.com", password="azerty")
        place = Place(name="hgh", host=user, description="well")
        review = Review(user=user, place=place, rating=5, comment="good")
        place.reviews.append(review)
        self.assertEqual(len(place.reviews), 1)
        self.assertEqual(place.reviews[0], review)

    def test_review(self):
        user = User(email="candidate@example.com", password="azerty")
        place = Place(name="The Best Place", host=user, description="good")
        review = Review(user=user, place=place, rating=5, comment="well done!")
        place.reviews.append(review)
        self.assertEqual(len(place.reviews), 1)
        self.assertEqual(place.reviews[0], review)


    def test_city_country(self):
        country = Country(name="France")
        city = City(name="Paris", country=country)
        self.assertEqual(city.name, "Paris")
        self.assertEqual(city.country, country)


if __name__ == '__main__':
    unittest.main()