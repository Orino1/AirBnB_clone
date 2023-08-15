#!/usr/bin/python3
"""
Test model
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    TestAmenity class: Test cases for the Amenity class.
    """

    def test_name(self):
        """ """
        user_obj = Amenity()
        self.assertEqual(type(user_obj.name), str)
