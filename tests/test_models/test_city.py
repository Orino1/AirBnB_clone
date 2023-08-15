#!/usr/bin/python3
"""
Test model
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test_User class: Test cases for the City class.
    """

    def test_name(self):
        """ """
        user_obj = City()
        self.assertEqual(type(user_obj.name), str)

    def test_state_id(self):
        """ """
        user_obj = City()
        self.assertEqual(type(user_obj.state_id), str)
