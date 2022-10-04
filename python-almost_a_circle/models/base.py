#!/usr/bin/python3
""" base """
import json


class Base:
    """ base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ It converts a list of dictionaries to a JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves a list of objects to a file in JSON format """
        newList = []
        if list_objs is not None:
            for currentObject in list_objs:
                newList.append(currentObject.to_dictionary())

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding='utf-8') as file:
            file.write(cls.to_json_string(newList))
