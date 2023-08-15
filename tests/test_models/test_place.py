#!/usr/bin/python3
"""
Test model
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    TestPlace class: Test cases for the Place class.
    """

    def test_name(self):
        """ """
        user_obj = Place()
        self.assertEqual(type(user_obj.name), str)

    def test_city_id(self):
        """ """
        user_obj = Place()
        self.assertEqual(type(user_obj.city_id), str)

    def test_user_id(self):
        """ """
        user_obj = Place()
        self.assertEqual(type(user_obj.user_id), str)

    def test_description(self):
        """ """
        user_obj = Place()
        self.assertEqual(type(user_obj.description), str)

    def test_number_rooms(self):
        """ """
        user_obj = Place()
        self.assertEqual(type(user_obj.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        user_obj = Place()
        self.assertEqual(type(user_obj.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        user_obj = Place()
        self.assertEqual(type(user_obj.max_guest), int)

    def test_price_by_night(self):
        """ """
        user_obj = Place()
        self.assertEqual(type(user_obj.price_by_night), int)

    def test_latitude(self):
        """ """
        user_obj = Place()
        self.assertEqual(type(user_obj.latitude), float)

    def test_longitude(self):
        """ """
        user_obj = Place()
        self.assertEqual(type(user_obj.longitude), float)

    def test_amenity_ids(self):
        """ """
        user_obj = Place()
        self.assertEqual(type(user_obj.amenity_ids), list)
