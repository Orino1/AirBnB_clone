#!/usr/bin/python3
"""
A basic State model.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from BaseModel.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize State class
        """
        super().__init__(*args, **kwargs)
