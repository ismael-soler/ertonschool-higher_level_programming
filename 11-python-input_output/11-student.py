#!/usr/bin/python3
""" Write a class Student """


class Student:
    """ Class Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dictionary info """
        dict_representation = self.__dict__
        if type(attrs) is list:
            new_dictionary = {}
            for attribute in attrs:
                for key, value in dict_representation.items():
                    if attribute == key:
                        new_dictionary[key] = value

            return new_dictionary
        return dict_representation

    def reload_from_json(self, json):
        """ reloads from json """
        self.__dict__.update(json)
