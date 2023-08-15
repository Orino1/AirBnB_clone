#!/usr/bin/python3
"""
TestFileStorage: Test cases for the FileStorage class.
TODO: we need to complete the description of the model here
"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    The description will be completed tomorrow.
    """
    def test_attributes(self):
        """
        The description will be completed tomorrow.
        """
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertTrue(hasattr(FileStorage, 'classes'))

    def test_new(self):
        """
        The description will be completed tomorrow.
        """
        file_storage = FileStorage()
        bm = BaseModel()
        file_storage.new(bm)
        key = f"{bm.__class__.__name__}.{bm.id}"
        self.assertTrue(key in file_storage._FileStorage__objects)

    def test_all(self):
        """
        The description will be completed tomorrow.
        """
        file_storage = FileStorage()
        all_objects = file_storage.all()
        self.assertEqual(type(all_objects), dict)
        self.assertIs(all_objects, file_storage._FileStorage__objects)

    def test_save_reload(self):
        """
        The description will be completed tomorrow.
        """
        file_storage = FileStorage()
        bm = BaseModel()
        file_storage.new(bm)
        file_storage.save()
        file_path = file_storage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path))
        file_storage.reload()
        all_objects = file_storage.all()
        self.assertTrue(isinstance(all_objects, dict))
        key = f"{bm.__class__.__name__}.{bm.id}"
        self.assertTrue(key in all_objects)


if __name__ == '__main__':
    unittest.main()
