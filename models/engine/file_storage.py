#!/usr/bin/python3


import json

class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):

        if obj:
            key = type(obj).__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):

        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open('FileStorage.__file_path', 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                f_dict = json.load(f)
                cls = '__class__'
                for key, value in f_dict.items():
                    FileStorage.__objects[key] = eval(value[cls] + '(**value)')
        except FileNotFoundError:
            pass
