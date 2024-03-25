#!/usr/bin/python3
"""
Module for FileStorage class.
"""
import json

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists).
        """
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                objs_dict = json.load(file)
                for key, value in objs_dict.items():
                    class_name, obj_id = key.split('.')
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass

