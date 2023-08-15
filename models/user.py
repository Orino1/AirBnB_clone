#!/usr/bin/python3
"""
This module defines the User class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Attributes:
        email (str): Email of the user.
        password (str): Password of the user.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
    Methods:
        __init__(*args, **kwargs):
            Initialize the User instance.
            Inherits attributes from BaseModel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize User class
        Args:
            *args: Variable length argument list (Not used at the moment).
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
