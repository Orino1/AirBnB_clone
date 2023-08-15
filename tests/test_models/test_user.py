#!/usr/bin/python3
"""
Test model
"""
import unittest
from models.user import User


class Test_User(unittest.TestCase):
    """
    Test_User class: Test cases for the User class.
    """

    def test_first_name(self):
        """ """
        user_obj = User()
        self.assertEqual(type(user_obj.first_name), str)

    def test_last_name(self):
        """ """
        user_obj = User()
        self.assertEqual(type(user_obj.last_name), str)

    def test_email(self):
        """ """
        user_obj = User()
        self.assertEqual(type(user_obj.email), str)

    def test_password(self):
        """ """
        user_obj = User()
        self.assertEqual(type(user_obj.password), str)
