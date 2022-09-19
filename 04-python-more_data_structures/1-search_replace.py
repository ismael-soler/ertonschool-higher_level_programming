#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return

    newList = [replace if elem == search else elem for elem in my_list]
    return newList
