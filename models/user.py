#!/usr/bin/python3
"""
A basic user model.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize User class
        """
        super().__init__(*args, **kwargs)
