#!/usr/bin/python3
"""
This module provides the FileStorage class, which manages
the storage of objects in a JSON file.
TODO: we need to complete the description of the model here.
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State


class FileStorage:
    """
    A class to manage the storage of objects in a JSON file.
        With the following attributes:
            __file_path: JSON file path
            __objects: a dictionary of objects (BaseModel)
    """

    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }
    def all(self):
        """
        Returns the dictionary of all objects currently stored.

        Return (dictionary): A dictionary (attribute __objects) containing
            all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage (__objects), as the following
        format: ex: to store a BaseModel object with id=12121212,
        the key will be BaseModel.12121212)

        Args:
            obj (BaseModel): The object to be added to the storage.

        No_return_value.
        """
        # Here should be a string reporesentation str not .to_dict()
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves the current state of the objects to the JSON file.

        No_return value.
        """
        # here we will save the object with .to_dict() so we can recreate them
        objects = FileStorage.__objects.copy()
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            for key, value in objects.items():
                objects[key] = value.to_dict()
            json.dump(objects, json_file)

    def reload(self):
        """
        Loads the objects from the JSON file, if the file exists.
        Note: if the file does not  exist no exception is raised.

        No_return_value.
        """
        # load the dict from json file > creat an object from dict(value)
        # then assigne the new object to __objects 
        objects = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                objects = json.load(json_file)
                for key, value in objects.items():
                    class_name = key.split('.')
                    # Avoiding 80 line max rule
                    cls_name = FileStorage.classes[class_name[0]]
                    FileStorage.__objects[key] = cls_name(**value)
