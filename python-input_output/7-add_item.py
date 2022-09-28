#!/usr/bin/python3
""" addas all arguments to Python list """
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"
with open(filename, 'a+', encoding='utf-8') as file:
    my_list = []
    args.pop(0)
    for elements in args:
        my_list.append(elements)
        save_to_json_file(my_list, filename)
        load_from_json_file(filename)
