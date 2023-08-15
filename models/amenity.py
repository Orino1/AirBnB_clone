#!/usr/bin/python3
"""
A basic Amenity model.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize Amenity class
        """

        super().__init__(*args, **kwargs)
