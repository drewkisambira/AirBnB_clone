#!/usr/bin/python3
"""
define class that serialisses instances to JSON and
deserilizes JSON fitle to instances
"""


import json


class FileStorage():
    """
    private class attributes
    """

   __file_path = "BaseModel.json"
    __objects = {}
    all_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    def all(self):
        """
        method returns dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        method sets in __objects and obj with key
        """

        if obj:
            key = type(obj).__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        method serializes __objects to JSON file
        """

        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open('FileStorage.__file_path', 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        method deserializes JSON file
        """

        try:
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                f_dict = json.load(f)
                cls = '__class__'
                for key, value in f_dict.items():
                    FileStorage.__objects[key] = eval(value[cls] + '(**value)')
        except FileNotFoundError:
            pass
