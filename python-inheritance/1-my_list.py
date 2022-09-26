#!/usr/bin/python3
""" write a class that inherits from list"""


class MyList(list):
    """ MyList """

    def print_sorted(self):
        lst = self.copy()
        lst.sort()
        print(lst)