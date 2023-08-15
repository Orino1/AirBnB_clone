#!/usr/bin/python3
"""
A basic City model.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize City class
        """
        super().__init__(*args, **kwargs)
