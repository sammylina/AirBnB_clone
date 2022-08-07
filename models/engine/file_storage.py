#!/usr/bin/python3
"""
    module for FileStorage
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
        "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """
        serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj
        
    def save(self):
        """
            serializes __objects to the JSON file(path: __file_path)
        """
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as json_file:
            json.dump(json_objects, json_file)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as json_file:
                jc = json.load(json_file)
            for key in jc:
                self.__objects[key] = classes[jc[key]["__class__"]](**jc[key])
        except:
            pass
