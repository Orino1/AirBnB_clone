#!/usr/bin/python3
"""
Test model
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test_User class: Test cases for the City class.
    """

    def test_user_id(self):
        """ """
        user_obj = Review()
        self.assertEqual(type(user_obj.user_id), str)

    def test_place_id(self):
        """ """
        user_obj = Review()
        self.assertEqual(type(user_obj.place_id), str)

    def test_text(self):
        """ """
        user_obj = Review()
        self.assertEqual(type(user_obj.text), str)
